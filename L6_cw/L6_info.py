import numpy as np

a=np.arange(2)
print(a)
b=np.array(a)
c=np.array([1,0])
print(b)
print(c)

pusta = np.empty((2, 2),dtype=int)
print(pusta)
# do elementów tablic możemy odwołać się tak jak do elementów np. listy czyli podając indeksy
poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]

# a teraz możemy utworzyć dwie macierze, najpierw wartości iterowane są w kolumnie a następnie w wierszu
z = np.indices((5, 3))
# wielowymiarowe macierze możemy również generować funkcją mgrid
x, y = np.mgrid[0:5, 0:5]
# print(z)
print(x)
print(y)

# podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
# w powyższym przykładzie stworzony wektor wartości zostanie umieszczony na głównej przekątnej macierzy
# możemy podać drugi parametr funkcji diag, który określa indeks przekątnej względem głównej przekątnej,
# która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(5)], -2)
print(mat_diag_k)