# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:35:29 2022

@author: Kriztoff
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# Read in dataset
trends = pd.read_csv('trends_kj_sisters.csv')

# Inspect data
trends.head()

# Make column names easier to work with
trends.columns = ['month', 'kim', 'khloe', 'kourtney', 'kendall', 'kylie'] #Se usan corchetes porque esta trabajando con una lista para renombrar las columnas

# Inspect data
trends.head()

for elemento in trends.columns:  #Ciclo for para recorrer cada elementod de el DF trends en cada columna
    # Only modify columns that have the "<" sign
    if '<' in trends[elemento].to_string():  #Si "caracter" en el recorrido de elemnto dentro de trends, pues to_string
        # Remove "<" and convert dtype to integer
        trends[elemento] = trends[elemento].str.replace('<', '') #por Cada valor que encontro en el if,en cada elemento, reemplaza '<' con '' 
        trends[elemento] = pd.to_numeric(trends[elemento]) #por cada valor que encontro en el ifm convierte a tipo numerico, cada elemnto

# Convert month to type datetime
trends['month'] = pd.to_datetime(trends['month']) # Dentro de trends, la columna 'month', ejecuta pandas.to_datetime en (la comluma trends(month) )
# Set month as DataFrame index
trends = trends.set_index('month')  #en Vez de dirigirlo directamente hubo que volverlo a asignar con trends =

# Inspect data types and data
trends.info()
trends.head()


trends.reset_index().plot(x = 'month', y=['kim','khloe', 'kourtney', 'kendall', 'kylie']) #al parecer hay un error si el index se deja en  month, por eso hay que reiniciarlo
trends.dtypes
trends.loc['2014-01-01':'2019-03-01'].reset_index().plot(x = 'month', y=['kim','khloe', 'kourtney', 'kendall', 'kylie'])

# Smooth the data with rolling means
trends_smooth= trends.rolling(window = 12).mean()
display(trends_smooth.tail())
trends_smooth.reset_index().plot(kind='line', x='month', y=['kim', 'khloe', 'kourtney', 'kendall', 'kylie'])

# Average search interest for each family line
trends['kardashian'] = (trends['kim']+ trends['kourtney'] + trends['khloe'])/3
trends['jenner'] = (trends['kendall'] + trends ['kylie'])/2
display(trends.head())
# Plot average family line search interest vs. month
trends[['kardashian','jenner']].reset_index().plot(kind='line', x='month', y =['kardashian','jenner'])
plt.ylabel('average interest by sisters')
plt.title('Kardashian vs. Jenner')