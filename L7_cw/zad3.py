import numpy as np

a = np.arange(1,4)
b = np.arange(4,7)
print(a,b,sep='\n')
print(a.dot(b))  # iloczyn macierzy
print(np.dot(a,b)) # inny sposób