import pandas as pd
import numpy as np

malla= pd.Series([ 
"No 4", #tamiz #4
"No 10", #tamiz #10
"No 20", #tamiz #20
"No 40", #tamiz #40
"No 60", #tamiz #60
"No 140", #tamiz #140
"No 200", #tamiz #200
"Fondo", #fondo
])

abertura = pd.Series([
4.75, #tamaño de la particula en mm tamiz numero 4
2, #tamaño de la particula en mm tamiz numero 10
0.85, #tamaño de la particula en mm tamiz numero 20
0.425, #tamaño de la particula en mm tamiz numero 40
0.25, #tamaño de la particula en mm tamiz numero 60
0.106, #tamaño de la particula en mm tamiz numero 140
0.075, #tamaño de la particula en mm tamiz numero 200
])

retenido = pd.Series([
15.5, #retenido en tamiz #4
25.8, #retenido en tamiz #10
60.5, #retenido en tamiz #20
40.2, #retenido en tamiz #40
41.2, #retenido en tamiz #60
15.2, #retenido en tamiz #100
13.2, #retenido en tamiz #200
15, #retenido en fondo
])


granulometria= pd.DataFrame({
    "malla": malla,
    "abertura": abertura, 
    "retenido": retenido 
})

granulometria["Ret_acumulado"] = granulometria["retenido"].cumsum()

granulometria["Ret_acumulado"].loc[7]

granulometria["pasa (g)"] = granulometria["Ret_acumulado"].loc[7] - granulometria["Ret_acumulado"]

granulometria["pasa (%)"] = granulometria["pasa (g)"]/granulometria["Ret_acumulado"].loc[7]*100

abertura_m= np.array(granulometria["abertura"]) #conjunto de valores
porcentaje_pasa = np.array(granulometria["pasa (%)"]) #conjunto de valores