class Parzyste:
    """Iterator zwracający tylko elementy 
        parzystych indeksow"""
    def __init__(self,zm):
        self.zm = zm
        self.index = -2
        # self.dl = 
    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index +2
        if self.index >= len(self.zm):
            raise StopIteration
        return self.zm[self.index]


kol=[2,1,2,1,2,1,2,1]
k=Parzyste(kol)
k22='kolejka'
k2=Parzyste(k22)
k.__iter__()
for i in range(0,len(kol),2):
    print(k.__next__())
print('#########################')
k2.__iter__()
for i in range(0,len(k22),2):
    print(k2.__next__())