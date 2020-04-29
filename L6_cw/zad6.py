# Stwórz skrypt który na wyjściu wyświetli macierz numpy 
# (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo będzie 
# wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów 
# powinno być wypisane od prawej do lewej.

#nwm
import numpy as np

s1='wyraz'
s2='yyrao'
s3='ryrar'
s4='ayrkr'
s5='zarbo'
sl1=np.array(list(s1),dtype='U1')
sl2=np.array(list(s2),dtype='U1')
sl3=np.array(list(s3),dtype='U1')
sl4=np.array(list(s4),dtype='U1')
sl5=np.array(list(s5),dtype='U1')

m = np.array([sl1,sl2,sl3,sl4,sl5])
print(m)