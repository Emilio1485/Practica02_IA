import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

# Abre el archivo CSV en modo lectura, se le da a la columna 1 el nombre de 'Texto' y la columna 2 el nombre de 'Etiqueta'
datos = pd.read_csv('ner_dataset.csv', names=['Texto', 'Etiqueta'])
datos1 = pd.read_csv('palabras_etiquetas.csv')

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
    # Crear un nuevo DataFrame con las palabras y etiquetas
    nuevo_datos = pd.DataFrame({'Palabra': [item[0] for sublist in palabras_etiquetas for item in sublist],
                            'Etiqueta': [item[1] for sublist in palabras_etiquetas for item in sublist]})

    # Se guarda en CSV
    nuevo_datos.to_csv('palabras_etiquetas.csv', index=False)

    # Imprimir las primeras filas del nuevo archivo
    print(nuevo_datos.head())



#Hace minusculas las palabras y muestra solamente una fila puesta en el input
def lower_eti_uno():
    i = int(input("Dame un número de o a 5559:\n"))
    datos['Texto']= datos['Texto'].str.lower().str.split()
    etiquetas = datos["Etiqueta"].tolist()
    palabras_etiquetas = [list(zip(texto, etiqueta.split())) for texto, etiqueta in zip(datos['Texto'], etiquetas)]
    datos["Palabras_Etiquetas"] = palabras_etiquetas
    print(datos['Palabras_Etiquetas'].iloc[i])

#Hace la separacion con train_test_split
def train_test_l():
    X = datos['Texto']
    y = datos['Etiqueta']
    #Minuculas
    datos['Texto']= datos['Texto'].str.lower().str.split()

    #Separación con train_test_split y imprime resultados
    X_train, X_eval, y_train, y_eval = train_test_split(X, y, test_size=0.3, random_state=42)
    print("Tamaño del conjunto de entrenamiento:", len(X_train))
    print("Tamaño del conjunto de evaluación:", len(X_eval))



# Funciones en acción
# imprimir_datos()
# lower_eti_uno()
train_test_l()


