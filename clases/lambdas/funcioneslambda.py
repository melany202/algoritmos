def linedesign (cantidad=60):
    print('#'*cantidad)

def sumar (a,b):
    suma = a+b
    return suma

def restar (a,b):
    resta = a-b
    return resta

def multiplicar (a,b):
    multiplicacion = a*b
    return multiplicacion

def dividir (a,b):
    division = a/b
    return division

def calculadora (funcion, a,b):
    return funcion (a,b)


linedesign(30)
print('Hola a todos')
linedesign(20)
print(sumar(2,6))
linedesign(30)
print(restar(5,3))
print(multiplicar(5,3))
print(dividir(5,3))
linedesign(30)
print(calculadora(sumar,12,14))

linedesignlambda = lambda cantidad=60 : print('#'*cantidad)
linedesignlambda()
sumarl = lambda a = 0 , b = 0 : a+b
print(sumarl(2,3))
linedesignlambda()
restal = lambda a = 0 , b = 0 : a-b
print(restal(34,9))
multiplicarl = lambda a = 0 , b = 0 : a*b
print(multiplicarl(3,9))
dividirl = lambda a = 0 , b = 0 : a/b
print(dividirl(12,6))

calculadoral = lambda func = restal,a = 0 , b = 0 : func(a,b)
print(calculadoral(multiplicarl, 68,62))

listaEdades= [18,12,14,13,12,20]
listaEdades2= [18,123,14,13,12,20]

lambdamaximos = lambda x = [] , y = [] : print(max(x),max(y)) 

lambdamaximos(listaEdades,listaEdades2)
mayorEdad = lambda edad = 0 : edad >=18
print(mayorEdad(14))
print(mayorEdad(19))
mayores = list (filter(mayorEdad,listaEdades))
print(mayores)



