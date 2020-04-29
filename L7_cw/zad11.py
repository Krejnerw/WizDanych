#Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. 
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. 
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
import numpy as np

a=np.arange(12)
print(a)
a=a.reshape((3,4))
b=a.reshape((4,3))
c=a.reshape((2,6))
a=a.ravel()
print(a)
b=b.ravel()
print(b)
c=c.ravel()
print(c)

