#fibonacci: 0,1,1,2,3,5,8,13,21,

#----preguntas----#
PREGUNTA_NUMERO = 'Ingrese numero entero : '

#----mensaje error----#
ERROR_ENTRADA = 'entrada no valida'
#----entradas----#
numero = None
while (numero == None):2
    try:
        numero = int (input(PREGUNTA_NUMERO))
    except ValueError:
            print(ERROR_ENTRADA)
print(numero)

numeroAnterior = 0
numeroActual = 1
if (numero == 1):
    print(numeroAnterior)
elif (numero == 2):
    print(numeroActual)
else:
    for i in range (2,numero+1):
        aux = numeroActual
        numeroActual = numeroAnterior + numeroActual
        numeroAnterior = aux
        print(numeroActual)
    print('salida',numeroActual)
        

