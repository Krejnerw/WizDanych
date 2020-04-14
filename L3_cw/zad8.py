def suma_C(a1=1, r=1, ile=10):
    suma=0.0
    for i in range(ile):
        suma+=a1
        a1+=r
    return suma
    
print(suma_C(1,1,1))
print(suma_C(1,1,3))
print(suma_C())

