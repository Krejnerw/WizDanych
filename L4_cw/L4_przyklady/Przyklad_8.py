class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        #deklarujemy atrybuty
        #self wskazuje że chodzi o zmienne właśnie definiowanej klasy
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


# Tworzymy obiekt
kwadrat= Ksztalty(10,30)

# Sprawdzamy teraz jak działają metody które zwracają wartość
print(kwadrat.pole())
print(kwadrat.obwod())

# sprawdzamy jak działają metody, które nie zwracają wartości
kwadrat.dodaj_opis("Kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.5)
print(kwadrat.x)
print(kwadrat.y)