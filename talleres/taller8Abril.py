#4,5,7,11,19
#numero1--->3 _(2**0)+3
#numero2---->5(2**1)+3
#numero3--->7(2**2)+3
#numero4--->(2**3)+3
#numero5--->(2**4)+3

def sucesion(n):
    return (2**(n-1))+3
print(sucesion(1))