import gradio as gr
from gradio import components
import pandas as pd 
import numpy as np
from datasets import load_dataset

# Lectura del CSV desde un data set
dataset = load_dataset("animonte/bank-state-data")
df = pd.DataFrame(dataset["train"])

def greet(name):
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
