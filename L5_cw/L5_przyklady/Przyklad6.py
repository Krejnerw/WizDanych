#4. Iteratory i generatory.

#Rozpatrując poniższy fragment kodu:

for element in range(1, 11):
    print(element)

#wszystko raczej jest jasne. Ale skąd pętla for wie jak 
# ma się uniwersalnie zachowywać dla różnych obiektów 
# iterowalnego ? Cały mechanizm jest obsługiwany przez 
# iteratory. W niewidoczny dla nas sposób pętle for 
# wywołuje funkcję iter() na obiekcie kolekcji. Funkcja 
# zwraca obiekt iteratora, który ma zdefiniowaną 
# metodę __next__(), odpowiedzialną za zwracanie kolejnych 
# elementów kolekcji. Kiedy nie ma już więcej elementów 
# kolekcji zgłaszany jest wyjątek StopIteration, kończący 
# działanie pętli for. Można wywołać funkcję __next__() 
# iteratora za pomocą wbudowanej funkcji next().

imie = "Reks"
it = iter(imie)
print(it)
# na wyjściu: <str_iterator object at 0x0000000003807FD0>
next(it)
# 'R'
next(it)
# 'e'
next(it)
# 'k'
next(it)
# 's'
next(it)
# Traceback (most recent call last):
#  File "<input>", line 1, in <module>
# StopIteration

#Przykład implementacji własnego iteratora.

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