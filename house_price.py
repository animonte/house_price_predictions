import gradio as gr
from gradio import components
import pandas as pd 
import numpy as np
from datasets import load_dataset

# Carga del CSV desde huggingface

dataset = load_dataset("animonte/train_house_price")

# Lectura del CSV desde un data set

df = pd.DataFrame(dataset["train"])

# Selección de variables para el modelo

Select = ['GrLivArea', 'TotalBsmtSF', 'MoSold', 'YearBuilt', 'YearRemodAdd', 'LotFrontage', 'YrSold', 'Id', 'BsmtFinSF1','OverallQual']
X = df.loc[:, Select ]  # Variables predictoras
y = df['SalePrice']     # Variable objetivo

# Interfaz gráfica del demo

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
