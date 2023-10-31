import csv

# Abre el archivo CSV en modo lectura
with open('ner_dataset.csv', 'r') as csv_file:
    # Lee el archivo CSV utilizando el módulo csv
    csv_reader = csv.reader(csv_file)

    lines = []

    #Seguimiento de la entidad actual
    entidad_actual = None

    # Recorre cada fila en el archivo CSV
    for row in csv_reader:
    
        etiqueta = row[0]

        if etiqueta == 'O':
            etiquetas_bio = 'O'
            entidad_actual = None
        elif etiqueta.startswith('B-Tag'):
            etiquetas_bio = etiqueta
            entidad_actual = etiqueta[2:]
        elif etiqueta.startswith('I-Tag'):
            if entidad_actual is not None and etiqueta[2:] == entidad_actual:
                etiquetas_bio = etiqueta
            else:
                etiquetas_bio = 'O'
                entidad_actual = None
        else:
            etiquetas_bio = 'O'

        # Agrega las líneas procesadas.
        lines.append([row[0], etiquetas_bio])
