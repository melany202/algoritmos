import pandas as pd 
dicPacientes = {}
dicPacientes['Enero'] = 32121
dicPacientes['Febrero'] =14564
dicPacientes['Marzo'] = 65465
dicPacientes['Abril'] = 85202
dicPacientes['Mayo'] = 93213
dicPacientes['Junio'] = 100231
dicPacientes['Julio'] = 120213
dicPacientes['Agosto'] = 65421
dicPacientes['Septiembre'] = 46546
dicPacientes['Octubre'] = 46547
dicPacientes['Noviembre'] = 84651
dicPacientes['Diciembre'] = 140521
dicPacientes['Diciembre'] = 123455096
seriePacientePorAño = pd.Series(dicPacientes)
print(seriePacientePorAño)

#muestren en pantalla los pacientes por cuatrimestre

dicPacientesCuatrimestre ={}
dicPacientesCuatrimestre['1er Cuatrimestre'] =(seriePacientePorAño['Enero':'Abril'])
dicPacientesCuatrimestre['2do Cuatrimestre'] =(seriePacientePorAño['Mayo':'Agosto'])
dicPacientesCuatrimestre['3er Cuatrimestre'] =(seriePacientePorAño['Septiembre':'Diciembre'])
seriesPacientesCuatrimestre = pd.Series(dicPacientesCuatrimestre)
print(seriesPacientesCuatrimestre)

from functools import reduce
lista = [32121,14564,65465,85202,93213,100231,120213,65421,46546,46547,84651,140521]
sumador = lambda acumulado = 0, elemento =0: acumulado + elemento
promedio = reduce (sumador,lista)/len(lista)
print(f'el promedio de pacientes atendidos es {promedio}')

dicEnfermedadesPorMes= {
    'Enfermedad general':[32121,14564,65465,85202,93213,100231],
    'COVID-19':[0,0,223,3453,4543,43643],
    'Traumatismos':[6545,43243,67657,435435,345345,43543],
    'Cancer':[6541,4334,4323,34545,5454,7675],
}
listaEnfermedades =['Enero','Febrero','Marzo','Abril','Mayo','Junio']
dataFrameEnfermedadesPorMes = pd.DataFrame(dicEnfermedadesPorMes, index = listaEnfermedades)
print(dataFrameEnfermedadesPorMes)

from functools import reduce
listaPacintesCovid =[3453,4543,43643]
sumador = lambda acumulado = 0, elemento =0: acumulado + elemento
promedio = reduce (sumador,listaPacintesCovid)/len(listaPacintesCovid)
print(f'el promedio de pacientes Covid durantes los meses abril,mayo,junio es {promedio}')

print(dataFrameEnfermedadesPorMes[['Cancer']]['Enero':'Marzo'])

print('pacientes con enfermedad general que superen los 40000')
listaPacientes = [32121,14564,65465,85202,93213,100231]
mayores = lambda elemento : elemento > 40000
listaMayores = list (filter(mayores, listaPacientes))
print (listaMayores)

print('multiplicar todos los pacientes de cancer por 0.1')
lista = [6541,4334,4323,34545,5454,7675]
multiplicar = lambda numero : numero *0.1
listaMultiplicar = list(map(multiplicar, lista))
print(listaMultiplicar)

print('suma de pacientes con traumatismos')
from functools import reduce
lista = [6545,43243,67657,435435,345345,43543]
sumar = lambda acumulado = 0, elemento = 0: acumulado + elemento
sumados = reduce (sumar, lista)
print (sumados)
