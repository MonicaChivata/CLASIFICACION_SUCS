import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .valoresentrada import *

def graficaGranulometria():
    fig = plt.figure(figsize=(15, 4.5)) #tamaño de la figura
    plt.plot(abertura_m,porcentaje_pasa,linestyle='-',marker='o', color='k', fillstyle='none',label='data') #graficamos abertura,porcentaje
    plt.xscale('log') #escala logarítmica en el eje x
    plt.xlabel('Particle size (mm)') #para el eje x colocar el nombre
    plt.ylabel('Percent finer(%)') #para el eje y colocar el nombre
    plt.title('Curva de granulometría') #para el título de la gráfica colocar el nombre
    plt.grid(color='k',lw='0.1',ls='-') #para hacer la grilla
    eje=plt.gca()
    eje.invert_xaxis() #invertir el eje x
    plt.grid(True)
    plt.ylim(-15,115) #establecer limites superior e inferior eje y

    plt.scatter(0.995331,60, marker='<', color='k',label='D60=1.0') #grafico de dispersion en el punto indicado
    plt.scatter(0.6971133,50, marker='s', color='k',label='D50=0.7') #grafico de dispersion en el punto indicado
    plt.scatter(0.3431044,30, marker='o', color='k',label='D30=0.34') #grafico de dispersion en el punto indicado
    plt.scatter(0.09167452,10, marker='>', color='k',label='D10=0.09') #grafico de dispersion en el punto indicado
    plt.legend(bbox_to_anchor=(1.12, 1), loc='upper right') #convenciones y las ubicamos por fuera de la gráfica

    x = [1, 10, 100, 5, 50, 20, 2, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001] #valores de la escala logaritmica en eje x
    plt.xticks(x, x, fontsize=10)
    # segundo eje x con número de tamices
    tamices = ["3","2-1/2","2","1-1/2","1","3/4","1/2","3/8","No. 4","No. 6","No. 8","No. 10","No. 16","No. 20","No. 30","No. 40","No. 50","No. 60","No. 80","No. 100","No. 140","No. 170","No. 200"]
    abertura_t=([75, 62, 50, 37.5, 25, 19, 12.5, 9.5, 4.75, 3.3, 2.35, 2, 1.165, 0.85, 0.6, 0.425, 0.3, 0.25, 0.18, 0.15, 0.106, 0.088, 0.075])
    ax2 = eje.twiny()
    ax2.set_xscale('log') #escala logaritmica
    ax2.set_xticks(abertura_t) 
    ax2.set_xticklabels(tamices, rotation=90,fontsize=10)
    ax2.set_xlim(0.001,100) #limite superior e inferior del eje x
    ax2.invert_xaxis() #invertimos eje x
    plt.axvline(x=75, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=75 desde -15 a 115 en el eje y
    plt.axvline(x=19, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=19 desde -15 a 115 en el eje y
    plt.axvline(x=4.75, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=4.75 desde -15 a 115 en el eje y
    plt.axvline(x=2, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=2 desde -15 a 115 en el eje y
    plt.axvline(x=0.425, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=0.425 desde -15 a 115 en el eje y
    plt.axvline(x=0.075, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=0.075 desde -15 a 115 en el eje y
    plt.axvline(x=0.01, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=0.01 desde -15 a 115 en el eje y
    plt.axvline(x=0.005, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=0.005 desde -15 a 115 en el eje y
    plt.axvline(x=0.00101, ymin=-15, ymax=115, color='grey', ls='--',lw='0.7') #linea vertical en x=0.00101 desde -15 a 115 en el eje y
    plt.text(87, -13, r'Cobble', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(22, -13, r'Gravel (Coarse)', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(5.5, -13, r'Gravel (Fine)', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(2.28, -13, r'Sand (Coarse)', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(0.49, -13, r'Sand (Medium)', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(0.087, -13, r'Sand (Fine)', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(0.0115, -13, r'Colloids', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(0.0058, -13, r'Silt', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.text(0.00118, -13, r'Clay', fontsize=10, rotation=90) #poner el texto en las coordenadas
    plt.grid(color='k',lw='0.1',ls='-') #grilla 
    plt.show() #muestra la grafica
