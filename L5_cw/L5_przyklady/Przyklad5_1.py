#Konstruktor klasy bazowej i dziedziczenie wielokrotne.
#Poniższy przypadek pokazuje ponownie dziedziczenie jednokrotne po klasie bazowej, gdzie mamy 3 klasy:

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko) 
        # --zwalnia z obowiazku pamietania klasy bazowej
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

#Zwróć uwagę na konstruktor klasy Pracownik, który wywołuje 
#konstruktor bazowej klasy Osoba. Natomiast w definicji 
# klasy Manadzer konstruktora nie ma a mimo to jestem w 
# stanie zainicjalizować obiekt tak jak obiekt Pracownik.