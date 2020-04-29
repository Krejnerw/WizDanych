import numpy as np

def funk(dl):
    b = np.arange(dl,0,-1, dtype='int64')
    return np.diag([a for a in b])

a=funk(3)
print(a)