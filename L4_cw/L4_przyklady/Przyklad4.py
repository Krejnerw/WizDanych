#klasy 

# class NazwaKlasy[(KlasaBazowa1, KlasaBazowa2, KlasaBazowa3)]:
#     instrukcje1
#     instrukcje2
#     instrukcjeN

#cos nie dziala
class PierwszaKlasa:
    """Przykład klasy"""
    atrybut = 54321

    def pierwsza_metoda(self, z):
        return "Teraz działa pierwsza Metoda"


obiekt = PierwszaKlasa()
print(obiekt)

#drukujemy atrybut
print(obiekt.atrybut)

#drukujemy metodę
print(obiekt.pierwsza_metoda())

#dodajemy atrybut do istniejącego obiektu
obiekt.tekst = "la la la"
print(obiekt.tekst)

#ale go nie będzie w nowej instancji klasy
nowy_obiekt = PierwszaKlasa()
print(nowy_obiekt.tekst)
