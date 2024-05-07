import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

#hue solo para scatter plot
def graficar(df, colx, coly, xlbl, ylbl, titl, clr, tipo, aux):
    plt.figure(figsize=(16, 9))
    
    if tipo == 'line':
        if aux is not None:
            grafica = sns.lineplot(x=colx, y=coly, data=df, color=clr, linewidth = 3, hue = aux)
        else:
            grafica = sns.lineplot(x=colx, y=coly, data=df, color=clr, linewidth = 3)
        plt.plot(df[colx], df[coly], marker='o', color=clr)
        plt.grid(True)
    elif tipo == 'bar':
        if aux is not None:
            colores = sns.color_palette(clr)
            grafica = sns.barplot(x=colx, y=coly, data=df, hue = aux, palette = colores)
            grafica.bar_label(grafica.containers[0], fontsize = 10, color = 'black')
            grafica.bar_label(grafica.containers[1], fontsize = 10, color = 'black')
            grafica.bar_label(grafica.containers[2], fontsize = 10, color = 'black')
            grafica.bar_label(grafica.containers[3], fontsize = 10, color = 'black')
            grafica.bar_label(grafica.containers[4], fontsize = 10, color = 'black')
            grafica.bar_label(grafica.containers[5], fontsize = 10, color = 'black')
        else:
            grafica = sns.barplot(x=colx, y=coly, data=df, color=clr)
            grafica.bar_label(grafica.containers[0], fontsize = 10)
    elif tipo == 'scatter':
        if aux is not None:
            grafica = sns.scatterplot(x=colx, y=coly, data=df, hue=aux)
        else:
            grafica = sns.scatterplot(x=colx, y=coly, data=df)        
            
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.title(titl)
    plt.xticks(rotation=45, ha='right')
    plt.show()


def grafica_pie(df, datos, keys, pallet_color, title, expl):
    aux = sns.color_palette(pallet_color)
    plt.pie(df[datos], labels = df[keys], colors = aux, autopct='%1.1f%%', explode = expl, wedgeprops = {"linewidth": 1, "edgecolor": "white"})
    plt.title(title)
    plt.show()


df_superstore = pd.read_csv('superstore_data.csv')
df_superstore.info()

