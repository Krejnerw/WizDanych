def Parzysta(zm):
    for ind in range(0,len(zm),2):
        yield zm[ind]

kol=Parzysta([2,1,2,1,2,1,2,1])

k22=Parzysta('kolejka')

print(next(kol))
print(next(kol))
print(next(kol))
print(next(kol))

print('#########################')

print(next(k22))
print(next(k22))
print(next(k22))
print(next(k22))
