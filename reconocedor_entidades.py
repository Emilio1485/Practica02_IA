import pandas as pd

# Abre el archivo CSV en modo lectura
datos = pd.read_csv('ner_dataset.csv', names=['Texto', 'Etiqueta'])

print(datos[:21])

datos['Etiqueta'] = datos['Etiqueta'].astype(str)

etiquetas_BIO = []
entidad_actual = None

# Recorre las filas del DataFrame
for etiqueta in datos['Etiqueta']:
    if etiqueta.startswith('O'):
        etiquetas_BIO.append('O')
        entidad_actual = None
    elif etiqueta.startswith('B-'):
        etiquetas_BIO.append('B-' + etiqueta[2:])
        entidad_actual = etiqueta[2:]
    elif etiqueta.startswith('I-'):
        if entidad_actual is not None and etiqueta[2:] == entidad_actual:
            etiquetas_BIO.append('I-' + entidad_actual)
        else:
            etiquetas_BIO.append('O')
            entidad_actual = None
    else:
        etiquetas_BIO.append('O')

# Agrega la lista de etiquetas BIO al DataFrame
datos['Etiqueta'] = etiquetas_BIO

print(datos[:21])