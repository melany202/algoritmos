
print('punto 2 parcial')
#formula del codigo : 8 + xyw + x + w

print('punto 3 del parcial')

print('A')
def sucesion(n):
    return (1/2**n)
print(sucesion(0))

print('B')
def sucesion(n):
    return (2*n)+3
print(sucesion(0))
print(sucesion(1))
print(sucesion(2))


print('punto 4 del parcial')

def contarPalabrasV1(parrafo):
  dictPalabrasOcurrencias = {}
  listaPalabras = parrafo.split()
  for palabra in listaPalabras:
    dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
  return dictPalabrasOcurrencias

def contarPalabrasV2(parrafo):
  dictPalabrasOcurrencias = {}
  listaPalabras = parrafo.split()
  for palabra in listaPalabras:
    dictPalabrasOcurrencias[palabra] = 0
    for i in range (len(listaPalabras)):
      if palabra == listaPalabras[i]:
        dictPalabrasOcurrencias[palabra] += 1
  return dictPalabrasOcurrencias

import time

inicio = time.time()
contarPalabrasV1('La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía. Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.Dos excesos: excluir la razón, no admitir más que la razón.Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.El hombre está dispuesto siempre a negar todo aquello que no comprende.Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.A fuerza de hablar de amor, uno llega a enamorarse.De qué le sirve al hombre ganar el mundo si pierde su alma?')
deltaV1 = time.time()-inicio
inicio =time.time()
contarPalabrasV2 =('La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía. Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.Dos excesos: excluir la razón, no admitir más que la razón.Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.El hombre está dispuesto siempre a negar todo aquello que no comprende.Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.A fuerza de hablar de amor, uno llega a enamorarse.De qué le sirve al hombre ganar el mundo si pierde su alma?')
deltaV2 = time.time()-inicio
print(deltaV1,deltaV2)

#justificacion : es mas rapido el segundo que el primero. el primero tiende a hacer mas lento porque lo que hace es una sumatoria de las palabras y despues al final reune las que se repite, por el contrario el segundo como se pone un condicional entonces va verificando si se repite desde el principio


