import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
c = np.cos(x)
s = np.sin(x)
plt.plot(x, s+2, label = 'siz(x)')
plt.plot(x, -s, label ='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(X)')
plt.title('Wykres sin(x), sin(x)')
plt.legend(loc=6)
plt.show()