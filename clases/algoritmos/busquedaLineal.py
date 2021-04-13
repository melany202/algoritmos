def busquedaLineal(lista,encontrar):
    isInList = False 
    for elemento in lista:
        if elemento == encontrar:
            isInList = True
    return isInList

listaEntrada= [2,12,34,5,11,59,4,3,1]
listaEntrada.sort()
valorEncontrar = int(input('ingrese un numero : '))
print(busquedaLineal(listaEntrada,valorEncontrar))
import busquedaBinaria as bi
import time 
encontrar = 59
inicio = time.time()
busquedaLineal(listaEntrada, encontrar)
deltaLineal = time.time()-inicio
inicio = time.time()
bi.busquedaBinaria(listaEntrada, encontrar)
deltaBinario = time.time()- inicio
print(deltaBinario,deltaLineal)

