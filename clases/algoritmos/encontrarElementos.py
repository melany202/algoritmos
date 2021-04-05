listaNombres = ['Karla','Arturo','Lauras','Juan']
print('Karla' in listaNombres)

encontro = False 
busqueda = 'Karla'
for elemento in listaNombres :
    if elemento == busqueda:
        encontro = True

print(encontro)
print(listaNombres.index('Arturo'))
posicion = None
for i in range (len(listaNombres)):
    if listaNombres[i] ==busqueda:
        posiicon = i
print(posicion)
