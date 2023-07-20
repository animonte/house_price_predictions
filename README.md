---
title: House Price Predictions
emoji: 🚀
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 3.36.1
app_file: house_price.py
pinned: false
license: gpl-3.0


## Segundo Proyecto personal

### Descripción del trabajo y el contexto:

Para poner en práctica los conocimientos en Modelos de aprendizaje *supervisado* he decidido sumergirme al desafío formativo al que nos invita la plataforma Kaggle. 

Parte de mi deseo era trabajar específicamente con Modelos que predigan un target numérico contínuo, para poder aplicar Regesión Lineal Múltiple específicamente y luego establecer comparaciones con otros algorítmos.

Con esta idea en mente, y luego de analizar los diferentes desafíos que nos propone Kaggle, he escogido **"House Price Predictions"** porque cumplía con estos objetivos planteados inicialmente.


### Ejecución de la tarea

#### 1. Exploración del DataFrame

En esta fase inicial, he tomado nota del problema en torno al mercado del Real Estate. Como no soy experta en esta materia, las decisiones que se toman por conocimiento del sector han sido a partir de averiguaciones en Internet y por razonamiento personal.

En la base de datos pude observar que las variables categóricas son un conjunto significativo frente al total de variables, lo cual siempre supone un desafío a la hora de pensarlas y tratarlas. Este ha sido el punto en el que he dedicado más pruebas para elegir la mejor forma de seleccionarlas.

La predicción de valores de propiedades en la base de datos que tenemos está sujeta a una ubicación geográfica específica, con lo cual será difícil traspolar el modelo aquí obtenido a otras jurisdicciones o Estados.

#### 2. Limpieza

Aquí he realizado todos los pasos de la fase de limpieza, he eliminado variables con porcentaje alto de nulos, he imputado valores faltantes cuando correspondía, he imputado valores a outliers.


#### 3. Selección de variables.

A las variables numéricas les he realizado una primera selección de acuerdo a la correlación con el target y colinealidad entre ellas.
Las variables categóricas las he seleccionado inicialmente por un razonamiento del mercado y luego las he transformado a dummies para poder incluirlas en el modelo

#### 4. Pruebas de modelos.

Primero subdividí el dataset para evitar el sobre-ajusto y luego he realizado pruebas con diferentes modelos: Regresión lineal múltiple, Ridge, Lasso, Random Forest, XGBooster. He elegido el que mejor desempeño tenía, **XGBOOSTER**.

#### 5. Acomodar datos para el demo

Para poder realizar un demo interactivo en donde un usuario pueda introducir sus valores y que la aplicación le devuelva el precio de la propiedad, debía reducir significativamente el número de variables porque sino el proceso del usuario resulta poco práctico incluso inviable.

He realizado una nueva selección de variables, escogiendo las que mi modelo ha considerado más predictivas. 

#### 6. Crear archivo para la interfaz visual

Luego de vincularme con un espacio de Hugging Face, he creado un archivo en el cual he incluido el modelo y luego lo he enviado a la interfaz gráfica con las variables correspondientes

#### 7. Tareas siguientes

La aplicación hugging face permite subir el modelo y conectarlo a la interfaz desde una API, sin embargo aún no he podido implementarlo de este modo. Esta tarea queda pendiente para seguir modificando este trabajo y mejorarlo

**NOTA:** El código borrador se encuentra en un archivo ipynb, que si bien está desordenado, muestra todo el proceso que no ha sido lineal, sino el resultado de múltiples pruebas y errores que me enfrentó el desafío. 

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
