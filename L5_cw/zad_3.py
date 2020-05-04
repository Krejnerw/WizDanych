#Poczytaj o metodach 
# __ge__, >=
# __gt__, >
# __le__, <=
# __lt__, <
# przeciąż je i spróbuj wykorzystać w instrukcji warunkowej 
# do porównania dwóch instancji obiektów klasy Kwadrat.

class Ksztalty:
    # definicja konstruktora
    #atrybut globalny
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

#wersja przeslonieta 
class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    def __add__(self, other):
        total_x = self.x + other.x
        return Kwadrat(total_x)

    def __ge__(self,other):
        if self.x >= other.x:
            return "Tak"
        else:
            return "nie"

    def __gt__(self,other):
        if self.x > other.x:
            return "Tak"
        else:
            return "nie"

    def __le__(self,other):
        if self.x <= other.x:
            return "Tak"
        else:
            return "nie"

    def __lt__(self,other):
        if self.x < other.x:
            return "Tak"
        else:
            return "nie"

#dokonczyc
kw = Kwadrat(5)
print(kw) #-->Kwadrat o boku 5

kw2=Kwadrat(7)
print(kw2)

kwkw2= kw + kw2
print(kwkw2)

tmp = Kwadrat(kw+kw2)
print(tmp)

print(tmp<kw)
print(tmp>=kw)