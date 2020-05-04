
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

print('jozek :')
print(isinstance(jozek,Osoba))#True
print(isinstance(jozek,Pracownik))#True
print(isinstance(jozek,Menadzer))#False
print('adrian :')
print(isinstance(adrian,Osoba))#True
print(isinstance(adrian,Pracownik))#True
print(isinstance(adrian,Menadzer))#True
#czy z lewej odwoluje sie do prawej
print('Osoba :')
print(issubclass(Osoba,Pracownik))#False
print(issubclass(Osoba,Menadzer))#False
print('Pracownik :')
print(issubclass(Pracownik,Osoba))#True
print(issubclass(Pracownik,Menadzer))#False
print('Menadzer :')
print(issubclass(Menadzer,Osoba))#True
print(issubclass(Menadzer,Pracownik))#True


