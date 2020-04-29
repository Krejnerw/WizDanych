import numpy as np
a= np.array([np.arange(3),np.arange(1,4),np.arange(2,5)])
b= np.array([np.arange(4),np.arange(1,5),np.arange(2,6),np.arange(3,7)])
print(a,"3x3")
print(b,"4x4")

print(a.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=1))
print(b.min(axis=0))