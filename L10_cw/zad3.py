import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
c = np.cos(x)
s = np.sin(x)
plt.plot(x, s, x, c)
ax = plt.subplot()
ax.annotate('sin(2*pi)',
            xy=(2*np.pi, 0),
            xytext=(0,1.2),
            arrowprops=dict(facecolor='black'))
ax.set_ylim(-1.5,1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['siz(x)','cos(x)'])
plt.show()