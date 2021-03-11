import pandas as pd
dicGanancia ={}
dicGanancia['Enero'] = 4000000
dicGanancia['Febrero'] = 5400000
dicGanancia['Marzo'] = 6700000
dicGanancia['Abril'] = 4780000
dicGanancia['Mayo'] = 5900000
dicGanancia['Junio'] = 3000000
dicGanancia['Julio'] = 6800000
dicGanancia['Agosto'] = 7000000
dicGanancia['Septiembre'] = 8300000
dicGanancia['Octubre'] = 5600000
dicGanancia['Noviembre'] = 9000000
dicGanancia['Diciembre'] = 7600000
seriesGananciaPorMes = pd.Series([4000000,5400000,6700000,4780000,5900000,3000000,6800000,7000000,8300000,5600000,9000000,7600000])
seriesGananciaPorMesDic = pd.Series (dicGanancia)
print(seriesGananciaPorMesDic['Enero':'Diciembre'])

dicIngestaPorMes = {
    'Enero' :[5,20,15,3,6],
    'febrero' :[4,12,20,3,5],
    'Marzo' :[2,4,6,4,10],
    'Abril' :[3,5,4,2,1],
    'Mayo' :[2,5,7,2,3],
    'Junio' :[3,2,4,5,1], 
    'Julio' :[2,7,4,2,5],
    'Agosto' :[2,5,3,1,6],
    'Septiembre' :[5,3,3,8,9],
    'Octubre' :[2,1,6,4,3],
    'Noviembre' :[5,6,3,2,1],
    'Diciembre' :[8,15,200,3,9]
}
dataFrameIngesta = pd.DataFrame (dicIngestaPorMes, index=['Pastas','Papitas','Carne asada','Maicitos','Platanito maduro'])
print(dataFrameIngesta)