import pandas as pd

# Abre el archivo CSV en modo lectura, se le da a la columna 1 el nombre de 'Texto' y la columna 2 el nombre de 'Etiqueta'
datos = pd.read_csv('ner_dataset.csv', names=['Texto', 'Etiqueta'])

#Imprime solammente una fila
def imprimir_elem_tabla():
    i = int(input("Dame un número de o a 5559:\n"))
    print("\nTabla:\n")
    print(datos.iloc[i])

#Imprime todos los datos
def imprimir_datos():
    print("\nTabla:\n")
    print(datos)

#Hace minusculas todas las palabras y muestra todas las filas del archivo
def lower_eti_all():
    datos['Texto']= datos['Texto'].str.lower().str.split()
    etiquetas = datos["Etiqueta"].tolist()
    palabras_etiquetas = [list(zip(texto, etiqueta.split())) for texto, etiqueta in zip(datos['Texto'], etiquetas)]
    datos["Palabras_Etiquetas"] = palabras_etiquetas
    print(datos['Palabras_Etiquetas'])

#Hace minusculas las palabras y muestra solamente una fila puesta en el input
def lower_eti_uno():
    i = int(input("Dame un número de o a 5559:\n"))
    datos['Texto']= datos['Texto'].str.lower().str.split()
    etiquetas = datos["Etiqueta"].tolist()
    palabras_etiquetas = [list(zip(texto, etiqueta.split())) for texto, etiqueta in zip(datos['Texto'], etiquetas)]
    datos["Palabras_Etiquetas"] = palabras_etiquetas
    print(datos['Palabras_Etiquetas'].iloc[i])
 

imprimir_datos()
lower_eti_uno()

