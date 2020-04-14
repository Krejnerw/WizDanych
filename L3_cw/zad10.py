def zlicz(**produkty):
    suma=0
    for x in produkty:
        suma+=produkty[x]
    return suma 
    
print(zlicz(marchew=4,cos=2,inne=6))
