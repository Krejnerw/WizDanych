import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
fig = plt.figure()

zs = 0
x = [10, 10, 25, 25, 30, 30, 38]
y = [20, 30, 30, 10, 10, 60, 60]

for  n, w, c in ([20,'scatter','r'],[5,'plot','g']):
    ax = fig.gca( projection = '3d' )
    xs = randrange(n, 0, 60)
    ys = randrange(n, 0, 100)
    if w=='scatter':
        ax.scatter(xs, ys, zs, zdir = 'z', c = c, marker = 'o')
    elif w=='plot':
        ax.plot(x, y, zs,c = c)
    ax.set_zlim(0,20)
    ax.set_xlabel( 'X' )
    ax.set_ylabel( 'Y' )
    ax.set_zlabel( 'Z' )
plt.show()