import pandas as pd

datos = pd.read_csv('ner_dataset.csv', names=['Texto', 'Etiqueta'])
etiquetas_BIO = []

entidad_actual = None

for etiqueta in datos['Etiqueta']:
    if etiqueta == 'O':
        etiquetas_BIO.append('O')
        entidad_actual = None

    elif etiqueta.startswith('B-Tag'):
        etiquetas_BIO.append('B-Tag' + etiqueta[2:])
        entidad_actual = etiqueta[2:]

    elif etiqueta.startswith('I-Tag'):

        if entidad_actual is not None and etiqueta[2:] == entidad_actual:
            etiquetas_BIO.append('I-Tag' + etiqueta[2:])
        else:
            etiquetas_BIO.append('O')
            entidad_actual = None

    else:
        etiquetas_BIO.append('O')


datos['Etiqueta-BIO'] = etiquetas_BIO


datos.to_csv('dataset_BIO_1.csv', index=False)