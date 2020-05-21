import matplotlib.pyplot as plt
import numpy as np

x= [1/y for y in range(1,21)]
plt.plot(x,'g>:', label='f(x)=1/x') 
plt.axis([0, 20, 0, 1])
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.legend()
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()