import gradio as gr
from gradio import components
import pandas as pd 
import numpy as np
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
import datetime



# Carga del CSV desde huggingface

dataset = load_dataset("animonte/train_house_price")

# Lectura del CSV desde un data set

df = pd.DataFrame(dataset["train"])

# Selección de variables para el modelo

columns = ['GrLivArea', 'TotalBsmtSF', 'MoSold', 'YearBuilt', 'YearRemodAdd', 'LotFrontage', 'YrSold', 'BsmtFinSF1','OverallQual']
X = df.loc[:, columns ]  # Variables predictoras
y = df['SalePrice']     # Variable objetivo

# División del dataframe para evitar el sobreajuste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Creamos una instancia con XGBClassifier
model_XGB = XGBRegressor(n_estimators=30, max_depth=2, learning_rate=.2, random_state=42)

#Entrenamos el modelo con los datos de entrenamiento
model_XGB.fit(X_train,y_train)

#Creamos el conjunto de entrenamiento
# prediction_XGB = model_XGB.predict(X_test)

# Interfaz gráfica del demo

def ui_predict(Superficie_casa, Superficie_sotano, Anio_construccion, Anio_remodelacion, Frente_terreno, Superficie_construida_terminada, calidad_construccion):

    # Obtener la fecha y hora actual
    fecha_actual = datetime.datetime.now()

    # Obtener el mes y el año de la fecha actual
    Mes_venta = fecha_actual.month
    Anio_venta = fecha_actual.year

    inputs = [[Superficie_casa, Superficie_sotano, Mes_venta, Anio_construccion, Anio_remodelacion, Frente_terreno, Anio_venta, Superficie_construida_terminada, calidad_construccion]]
    inputs = pd.DataFrame(inputs, columns= columns)
    # Predicción
    predicciones = model_XGB.predict(inputs)

    return predicciones[0]

output = components.Textbox(label='Precio obtenido con el XG BOOST Regressor')

demo = gr.Interface(
    fn=ui_predict, 
    inputs=['number', "number","number","number", "number","number", gr.Slider(1, 10, step=1)], 
    outputs=output, 
    allow_flagging="never"
    )

demo.launch()