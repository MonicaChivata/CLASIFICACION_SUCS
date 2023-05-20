import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

def graficaPlasticidad(LL,IP):
  lineaA = np.array([0,58.4]) #conjunto de valores desde 0 hasta 58.4
  lineaU = np.array([0,60.3]) #conjunto de valores desde 0 hasta 60.3
  LL = np.array([20,100]) #conjunto de valores desde 20 hasta 100
  limite_liquido = np.array([8,75]) #conjunto de valores de 8 a 75
  a = [16,50,50,29] #conjunto de puntos en el eje x
  b = [7,38,22,7] #conjunto de puntos en el eje y
  d = [20,50,50] #conjunto de puntos en el eje x
  e = [0,22,0] #conjunto de puntos en el eje y
  f = [50,50,80,100,100,50] #conjunto de puntos en el eje x
  g = [0,22,44,58.4,0,0] #conjunto de puntos en el eje y
  h = [50,50,75,100,100,50] #conjunto de puntos en el eje x
  i = [22,38,60,60,58.4,22] #conjunto de puntos en el eje y
  j = [12.5,16,30,25] #conjunto de puntos en el eje x
  k = [4,7,7,4] #conjunto de puntos en el eje y
  l = [8,12.5,25,20] #conjunto de puntos en el eje x
  m = [0,4,4,0] #conjunto de puntos en el eje y
  plt.plot(LL,lineaA, 'b-', label = "Linea A") #graficamos LL contra lineaA, se nombra como Linea A y será de color azul.
  plt.plot(limite_liquido, lineaU, 'k', ls=':', label = "Linea U") #graficamos limite_liquido contra lineaU, se nombra como Linea U, color negro y la linea punteada : 
  plt.axvline(x=50, ymin=0, ymax=60, color='g') #linea vertical en x=50 desde 0 a 60 en el eje y, color verde.
  plt.axvline(x=80, ymin=0, ymax=60, color='k', ls='--') #linea vertical en x=80 desde 0 a 60 en el eje y, color negro, linea punteada
  plt.axhline(y=20, xmin=0, xmax=100, color='k', ls='--') #linea horizontal en y=20 desde 0 a 100 en el eje x, color negro, linea punteada
  plt.text(9, 20, r'LP', fontsize=10) #poner el texto LP en las coordenadas (9,20)
  plt.text(15, 35, r'NO EXISTE', fontsize=10) #poner el texto NO EXISTE en las coordenadas (15,35)
  plt.text(31, 15, r'CL', fontsize=10) #poner el texto CL en las coordenadas (31,15)
  plt.text(15, 5, r'CL-ML', fontsize=10) #poner el texto CL-ML en las coordenadas (15,5)
  plt.text(35, 5, r'ML', fontsize=10) #poner el texto ML en las coordenadas (35,5)
  plt.text(80, 20, r'MH', fontsize=10) #poner el texto MH en las coordenadas (80,20)
  plt.text(81, 55, r'LL', fontsize=10) #poner el texto LL en las coordenadas (81,55)
  plt.text(62, 40, r'CH', fontsize=10) #poner el texto CH en las coordenadas (62,40)
  plt.fill(a, b, facecolor='burlywood', alpha=0.5) #permite sombrear el poligono delimitado por las coordenadas (a,b) 
  plt.fill(d, e, facecolor='grey', alpha=0.5) #permite sombrear el triangulo delimitado por las coordenadas (d,e) de color gris
  plt.fill(f, g, facecolor='hotpink', alpha=0.5) #permite sombrear el poligono delimitado por las coordenadas (f,g) de color rosado
  plt.fill(h, i, facecolor='lime', alpha=0.5) #permite sombrear el poligono delimitado por las coordenadas (h,i) de color lima
  plt.fill(j, k, facecolor='magenta', alpha=0.5) #permite sombrear el poligono delimitado por las coordenadas (j,k) de color magenta
  plt.fill(l, m, facecolor='grey', alpha=0.5) #permite sombrar el poligono delimitado por las coordenadas (l,m) de color gris
  plt.grid(color='k',lw='0.1',ls='-') #permite hacer la grilla en color negro, con linea continua ls=-
  plt.title("CARTA DE PLASTICIDAD", fontsize=10) #titulo del grafico en tamaño de letra 10
  plt.xlabel("Limite Liquido",fontsize=10) #para el eje x colocar el nombre Limite Liquido, el tamaño de la letra será de 10
  plt.ylabel("Indice de Plasticidad",fontsize=10) #para el eje y colocar el nombre Indice de Plasticidad, el tamaño de la letra será de 10
  plt.scatter(80,20,c="red") #grafico de dispersion en el punto (80,20) y se muestra en color rojo
  plt.legend() #muestra las convenciones
  plt.xlim(0,100) #con esta funcion establecemos el limite superior e inferior del eje x
  plt.ylim(0,60) #con esta funcion establecemos el limite superior e inferior del eje y
  plt.show() #mostrar el grafico