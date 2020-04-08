from random import random
macierz = [[round(random()*100) for x in range(4)]for y in range(4)]
print(macierz)
przekatna=[macierz[x][x]for x in range(4)]
print(przekatna)