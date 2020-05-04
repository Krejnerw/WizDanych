#Za pomocą funkcji isinstance() oraz issubclass() sprawdź wynik dla instancji obiektu Pracownik oraz Menadzer dla klas Osoba, Pracownik i Manadzer.

#Zwróć uwagę na poniższy przykład dziedziczenia wielokrotnego i konstruktor.

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:

    def __init__(self, pensja):
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

#kolejnosc dziedziczenia ma znaczenie 
# ostatnia przeslania wczesniejsze
class Menadzer(Osoba, Pracownik):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)
        # super().__init__(imie, nazwisko)
        #tutaj super juz nie mozna uzyc

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
print(adrian.przedstaw_sie())