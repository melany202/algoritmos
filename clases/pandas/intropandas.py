import pandas as pd
listaVariada=['a',1,2,4.6]
print (listaVariada)
seriesPandas = pd.Series ([1,2,5])
print(seriesPandas)
seriesPandas = pd.Series ([4.6,5.7,0.1])
print(seriesPandas)
dicGanancia ={}
dicGanancia['Enero'] = 4300
dicGanancia['Febrero'] = 4545
dicGanancia['Marzo'] = 2324
dicGanancia['Abril'] = 1244
seriesGananciaPorMes = pd.Series([4300,4545,2324,1244])
print(seriesGananciaPorMes)
seriesGananciaPorMesDic = pd.Series (dicGanancia) 
print(seriesGananciaPorMesDic['Enero':'Marzo'])
print(seriesGananciaPorMesDic['Febrero':'Marzo'])



matrizEstudiantes = {
                        'Grupo1' : ['Karla', 'Mario', 'Laura'],
                        'Grupo2' : ['Santi', 'Arturo', 'Vale'],
                        'Grupo3' : ['Juan', 'Melany', 'Laura'],
                        'Grupo4' : ['Mafer', 'Esteban','Daniel'],
}
dataFrameNombres = pd.DataFrame(matrizEstudiantes)
print (dataFrameNombres)

print(dataFrameNombres['Grupo2'])
print(dataFrameNombres.iloc[1:2])

dicVentasPorMes = {
    'Marzo(millones de pesos)' :[1234,4235,3356],
    'Abril(millones de pesos)' :[1234,42355,7356],
    'Mayo(millones de pesos)' :[4234,4635,1356]
}
dataFrameVentas = pd.DataFrame (dicVentasPorMes, index=['Tomates','Papas','Yuca'])
print(dataFrameVentas)
print(dataFrameVentas.iloc[:2])

