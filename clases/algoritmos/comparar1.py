import time 
import ordenamientoBurbuja as ob 
import ordenamientoPorInsercion as oi

lista = [2,1,8,6,4]
listaCopia = lista.copy()

##inicio
inicio = time.time()

#instrucciones
ob.ordenamientoBurbuja(lista)

#delta
deltaOb = time.time() - inicio

##inicio
inicio = time.time()

#instrucciones 
listaCopia.sort()

#delta
deltaSort = time.time()-inicio
print(deltaSort)
print(deltaOb)
print(deltaSort >= deltaOb)

##inicio
inicio = time.time()

#instrucciones 
oi.ordenamiento_insercion(lista)

#delta
deltaOi = time.time() - inicio 

print(deltaSort)
print(deltaOb)
print(deltaOi)
print(deltaSort >= deltaOb)
print(deltaSort >= deltaOi)




