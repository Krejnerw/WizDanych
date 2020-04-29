#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla 
# każdej z jej wartości i zapisz do zmiennej “a”.

#Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus 
# dla każdej z jej wartości i zapisz do zmiennej “b”.

#Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do 
# zmiennych a i b.
import numpy as np
#zle

x = np.arange(6).reshape(2,3)
print(x)
a=np.sin(x)
b=np.cos(x)
print(a)
print(b)
print(a+b)