from .cartaplasticidad import *
from .valoresentrada import *
from .granulometria import *

tamiz_200 = 114
tamiz_4 = 8
Cc = 1
Cu = 4

def cartaPlasticidad():
  LL=int(input("Por favor ingrese el limite liquido")) #le pedimos al usuario que ingrese el limite liquido
  IP=int(input("Por favor ingrese el indice de plasticidad")) #le pedimos al usuario que ingrese el indice de plasticidad
  lineaA=0.73*(LL-20) #ecuacion linea A
  print(lineaA)
  lineaU=0.9*(LL-8) #ecuacion linea U
  print(lineaU)
  if LL>50: #Mundo de los alta plasticidad
    if 0 < IP < lineaA:
      print("MH")
      graficaPlasticidad(LL,IP)
    elif lineaA < IP < lineaU:
      print("CH")
      graficaPlasticidad(LL,IP)
    else: #se utiliza para proporcionar una acción alternativa cuando una condición "if" no se cumple
      print("No existe")
      graficaPlasticidad(LL,IP)
  else: #Mundo de los baja plasticidad
    if 0 < IP < lineaA:
      print("ML")
      graficaPlasticidad(LL,IP)
    elif lineaA < IP < lineaU:
      print("CL")
      graficaPlasticidad(LL,IP)
    else: #se utiliza para proporcionar una acción alternativa cuando una condición "if" no se cumple
      print("No existe")
      graficaPlasticidad(LL,IP)

def clasificacion():
  if tamiz_200 > 50: #Mundo Finos
    cartaPlasticidad()
  else: #Mundo Gruesos
    if tamiz_4 > 50: #Mundo Arenas
      if tamiz_200<5: 
        if Cu>=6 and 1<=Cc<=3: #Cu debe ser mayor a 6 y Cc debe estar entre 1 y 3
          print("SW") #imprimir SW
          graficaGranulometria()
        else: #se utiliza para proporcionar una acción alternativa cuando una condición "if" no se cumple
          print("SP") #imprimir SP
          graficaGranulometria()
      elif tamiz_200>12: 
        if Cu>=6 and 1<=Cc<=3:
          print("SM")
          graficaGranulometria()
        else:
          print("SC")
          graficaGranulometria()
    else: #Mundo Gravas
      if tamiz_200<5:
        if Cu>=4 and 1<=Cc<=3:
          print("GW")
          graficaGranulometria()
        else: #se utiliza para proporcionar una acción alternativa cuando una condición "if" no se cumple
          print("GP")
          graficaGranulometria()
      elif tamiz_200>12:
        if Cu>=4 and 1<=Cc<=3:
          print("GM")
          graficaGranulometria()
        else: #se utiliza para proporcionar una acción alternativa cuando una condición "if" no se cumple
          print("GC")
          graficaGranulometria()