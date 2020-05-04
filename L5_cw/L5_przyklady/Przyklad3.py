#3. Atrybuty globalne, 'pusta' klasa oraz ponownie zmienna 'prywatna'
#Nawiązując do wprowadzenia do programowania obiektowego 
#w języku Python należy wspomnieć o możliwości stworzenia 
# atrybutów współdzielonych przez wszystkie instancje danej klasy.

class Point:
    # 1 zmienna dzielona przez wszystkie obiekty
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)
p1.update(2)
print(p1.counter)
print(p2.counter)