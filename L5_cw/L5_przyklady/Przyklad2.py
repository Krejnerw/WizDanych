#2. Przesłanianie metod.
#Przykład przesłaniania metody został przedstawiony w 
# przykładzie 1, ale warto dodać, że możemy również 
# przesłaniać metody i zmienne dziedziczone po superklasie 
#bazowej object, czyli tej, po której dziedziczy każdy 
# obiekt w Pythonie. Możemy np. przeciążyć metodę __str__(), 
# która zwraca tekstową reprezentację obiektu i domyślnie 
# wyświetla informację o typie obiektu oraz adresie 
# zajmowanym w pamięci komputera.

#__str__() jest dziedziczony od obiektu
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

# class Kwadrat(Ksztalty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x

# kw = Kwadrat(5)
# print(kw)
# #__str__() wypisz cos w stylu 
# #<__main__.Kwadrat object at 0x01467190>

#wersja przeslonieta 
class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
kw = Kwadrat(5)
print(kw) #-->Kwadrat o boku 5
