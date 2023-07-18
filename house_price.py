import gradio as gr
from gradio import components
import pandas as pd 
import numpy as np
from datasets import load_dataset

# Carga del CSV desde huggingface

dataset = load_dataset("animonte/train_house_price")

# Lectura del CSV desde un data set

df = pd.DataFrame(dataset["train"])



# Interfaz gráfica del demo

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
