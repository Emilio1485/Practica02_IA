import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from hmmlearn.hmm import CategoricalHMM
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer


# Abre el archivo CSV en modo lectura, se le da a la columna 1 el nombre de 'Texto' y la columna 2 el nombre de 'Etiqueta'
datos = pd.read_csv('ner_dataset.csv', names=['Texto', 'Etiqueta'])
datos['Etiqueta'] = datos['Etiqueta'].astype(str)

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
    etiquetas = datos['Etiqueta'].tolist()
    palabras_etiquetas = [list(zip(texto, etiqueta.split())) for texto, etiqueta in zip(datos['Texto'], etiquetas)]
    datos['Palabras_Etiquetas'] = palabras_etiquetas

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

    markov(X_train, X_eval)
    

def markov(X_train, x_eval):
    # Crear un codificador de etiquetas para convertir etiquetas de texto a valores numéricos
    label_encoder = LabelEncoder()
    vectorizer = CountVectorizer()
    X_train_numeric_sparse = vectorizer.fit_transform(X_train)

    # Convertir la matriz dispersa en una matriz densa
    X_train_numeric = X_train_numeric_sparse.toarray()
    # Crear un modelo HMM
    hmm_model = CategoricalHMM(n_components=500, random_state=42)
    # Entrenar el modelo HMM
    hmm_model.fit(X_train_numeric)

    # Imprimir la matriz de transición entre estados ocultos
    print("Matriz de Transición entre Estados Ocultos:")
    print(hmm_model.transmat_)
    # Imprimir las probabilidades de emisión de observaciones por estado oculto
    print("Probabilidades de Emisión de Observaciones por Estado Oculto:")
    print(hmm_model.emissionprob_)

    imprimir_viterbi(viterbi(x_eval,hmm_model))

    ej6(X_train)

#funcion viterbi
def viterbi(X_eval, hmm_model):
    etiquetas_predichas = []

    for secuencia in X_eval:
        secuencia_predicha = hmm_model.predict(secuencia.reshape(-1, 1))
        etiquetas_predichas.append(secuencia_predicha)

    return etiquetas_predichas

    # Obtener las etiquetas 
    etiquetas_predichas = obtener_etiquetas_viterbi(X_eval, hmm_model)

def imprimir_viterbi(etiquetas):
    print("Etiquetas Predichas para las Primeras Secuencias:")
    for i in range(10):  # Imprime las etiquetas de las primeras 10 secuencias
        print(etiquetas[i])

def ej6(X_train):
    # Entrenar un modelo HMM con los datos de entrenamiento
    modelo_hmm = hmm.MultinomialHMM(n_components=3) 
    modelo_hmm.fit(X_train)

    # Obtiene las predicciones
    etiquetas_predichas = modelo_hmm.predict(X_eval)

    # Compara las predicciones
    informe_clasificacion = classification_report(y_eval, etiquetas_predichas)
    print("Informe de Clasificación:\n", informe_clasificacion)


#imprimir_datos()

lower_eti_all()
    
#train_test_l()


