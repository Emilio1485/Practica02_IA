import pandas as pd
from sklearn.model_selection import train_test_split

# Abre el archivo CSV en modo lectura, se le da a la columna 1 el nombre de 'Texto' y la columna 2 el nombre de 'Etiqueta'
datos = pd.read_csv('ner_dataset.csv', names=['Texto', 'Etiqueta'])

#Imprime solamente una fila
def imprimir_elem_tabla():
    i = int(input("Dame un número de 0 a 5559:\n"))
    print("\nTabla:\n")
    print(datos.iloc[i])

#Imprime todos los datos
def imprimir_datos():
    print("\nTabla:\n")
    print(datos)

#Hace minúsculas todas las palabras y muestra todas las filas del archivo
def lower_eti_all():
    datos['Texto'] = datos['Texto'].str.lower().str.split()
    etiquetas = datos["Etiqueta"].tolist()
    palabras_etiquetas = [list(zip(texto, etiqueta.split())) for texto, etiqueta in zip(datos['Texto'], etiquetas)]
    datos["Palabras_Etiquetas"] = palabras_etiquetas
    print(datos['Palabras_Etiquetas'])

#Hace minúsculas las palabras y muestra solamente una fila puesta en el input
def lower_eti_uno():
    i = int(input("Dame un número de 0 a 5559:\n"))
    datos['Texto'] = datos['Texto'].str.lower().str.split()
    etiquetas = datos["Etiqueta"].tolist()
    palabras_etiquetas = [list(zip(texto, etiqueta.split())) for texto, etiqueta in zip(datos['Texto'], etiquetas)]
    datos["Palabras_Etiquetas"] = palabras_etiquetas
    print(datos['Palabras_Etiquetas'].iloc[i])

# Hace minúsculas las palabras
datos['Texto'] = datos['Texto'].str.lower()

# Separar los datos en características (X) y etiquetas (y)
X = datos['Texto']
y = datos['Etiqueta']

# Separar los datos en un 70% de entrenamiento y un 30% de evaluación
X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=0.3, random_state=42)

# Imprimir tamaños de los conjuntos de entrenamiento y evaluación
print("Tamaño del conjunto de entrenamiento:", len(X_train))
print("Tamaño del conjunto de evaluación:", len(X_eval))

# Llama a las funciones que proporcionaste
# imprimir_datos()
# lower_eti_uno()
