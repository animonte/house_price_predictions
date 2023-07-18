import gradio as gr
from gradio import components
import pandas as pd 
import numpy as np
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor


# Carga del CSV desde huggingface

dataset = load_dataset("animonte/train_house_price")

# Lectura del CSV desde un data set

df = pd.DataFrame(dataset["train"])

# Selección de variables para el modelo

Select = ['GrLivArea', 'TotalBsmtSF', 'MoSold', 'YearBuilt', 'YearRemodAdd', 'LotFrontage', 'YrSold', 'Id', 'BsmtFinSF1','OverallQual']
X = df.loc[:, Select ]  # Variables predictoras
y = df['SalePrice']     # Variable objetivo

# División del dataframe para evitar el sobreajuste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Creamos una instancia con XGBClassifier
model_XGB = XGBRegressor(n_estimators=30, max_depth=2, learning_rate=.2, random_state=42)

#Entrenamos el modelo con los datos de entrenamiento
model_XGB.fit(X_train,y_train)

#Creamos el conjunto de entrenamiento
prediction_XGB = model_XGB.predict(X_test)

#Calculamos la puntuación con el conjunto de entrenamiento
scoreR2_XGB = r2_score(y_test, prediction_XGB)

print("Puntuación:", scoreR2_XGB)

# Interfaz gráfica del demo

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
