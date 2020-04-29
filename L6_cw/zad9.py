#Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz 
# macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.
import numpy as np

def fib(i):
    if i==0:
        return 0
    if i==1 or i==2:
        return 1
    return fib(i-1)+fib(i-2)


a=np.array([fib(i) for i in range(25)])
a=a.reshape((5,5))
print(a)

