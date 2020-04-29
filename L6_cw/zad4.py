import numpy as np

def funk(pdst,do):
    return np.logspace(1,do,num=do,base=pdst,dtype='int64')

a=funk(2,4)
print(a)