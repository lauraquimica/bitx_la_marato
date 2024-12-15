﻿# bitx_la_marato
 # 1r Tenemos la base de datos en Excel
 # 2n Tenemos el codigo principal python, donde preprocesamos toda la base de datos, eliminamos variables redundantes o que no afectan a la variable objetivo.
 # 3r Hacemos miramos el balanceo de las clases, hacemos one-hot encoding y reducción de las variables con PCA.
 # 4t Entrenamos 4 modelos con sus mejores hiperparametros con cross-validation, para luego probarlo con el conjunto test y obtener el mejor modelo.
 #EXTRA: hemos empoecado a implementar la calculadora de predicción, la cual coje los datos de un paciente actual y el codigo preprocesara sus variables para luego implementar el modelo a los datos para que predizca si empeorar o se mantendra estable. Aunque faltaria combinar la parte visual de la pestaña interactiva con el codigo que implementa los datos para el modelo
