
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
k11=[15,47,3,0,7]
k1=Wspak(k11)
k22='kolejka'
k2=Wspak(k22)
k33=['g',7,'ok',9,0]
k3=Wspak(k33)
k1.__iter__()
for i in k11:
    print(k1.__next__())
print('#########################')
k2.__iter__()
for i in k22:
    print(k2.__next__())
print('#########################')
k3.__iter__()
for i in k33:
    print(k3.__next__())
print('#########################')