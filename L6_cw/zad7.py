import numpy as np

#funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i 
# umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących 
# się od głównej przekątnej.

def funk(n):
    mac=np.diag([-2 for a in range(n)])
    for i in range(n):
        mac+=np.diag([2+2*i for a in range(n-i)],i)
        mac+=np.diag([2+2*i for b in range(n-i)],-i)
    return mac

print(funk(3),funk(4),sep='\n')