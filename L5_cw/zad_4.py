# Korzystając z powyższego kodu stwórz kilka instancji klasy 
# Point i spróbuj odwołać się do zmiennej counter z poziomu 
# różnych instancji, porównując jej wartość dla każdej z nich 
# oraz spróbuj zmienić jej wartość.

# Ciekawostką jest to, że możemy stworzyć „pustą” klasę tylko 
# po to, żeby przechować wartość wielu zmiennych w pojedynczej 
# referencji, coś jak struktura w języku C.
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(3,0)
p4 = Point(0,4)

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)
print('########################')
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')
p1.update(1)
p2.update(2)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')
p3.update(0)
p4.update(3)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')
p3.counter=[1,2]
p4.counter=p3.counter
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')
Point.counter=[1,3]
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')
p4.update(5)
Point.counter=[1,6,6]
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')
p4.counter=p1.counter
Point.counter=[1,6,6]
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print('########################')