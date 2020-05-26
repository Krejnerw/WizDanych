#Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem różnych znaczników i kolorów:
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680801 )
def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
n = 100


for c, m, zlow, zhigh in [('yellowgreen', 'o', -50, -40),( 'cyan' , '|' , - 40 , - 5 ),( 'b' , 'x', -10, 20 ),('yellow', '*', 0, 20),('r', '.', -50, -40)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow,zhigh)
    ax.scatter(xs,ys,zs,c = c, marker = m)

ax.set_xlabel('X Lab')
ax.set_ylabel('Y Lab')
ax.set_zlabel('Z Lab')
plt.show()