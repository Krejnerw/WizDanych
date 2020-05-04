#Przeciąż metodę __add__() dla klasy Kwadrat, 
# która będzie zwracała instancje klasy Kwadrat o nowym 
# boku, będącym sumą boków dodawanych do siebie kwadratów.

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


#dokonczyc
kw = Kwadrat(5)
print(kw) #-->Kwadrat o boku 5

kw2=Kwadrat(7)
print(kw2)
kwkw2= kw + kw2
print(kwkw2)
