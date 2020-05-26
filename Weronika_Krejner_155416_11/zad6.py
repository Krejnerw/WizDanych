import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
fig = plt.figure()

ax1 = fig.add_subplot( 121 , projection = '3d' )
ax2 = fig.add_subplot( 122 , projection = '3d' )
for i, n, w, c in ([121,20,'scatter','r'],[122,5,'plot','b']):
    ax = fig.add_subplot( i , projection = '3d' )
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, 0,0)
    if w=='scatter':
        ax.scatter(xs,ys,zs,c = c, marker = 'o')
    elif w=='plot':
        ax.plot(xs,ys,zs,c = c, marker = 'o')
plt.show()