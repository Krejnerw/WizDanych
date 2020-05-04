# Korzystając z powyższego kodu stwórz kilka instancji klasy Point i spróbuj odwołać się do zmiennej counter z poziomu różnych instancji, porównując jej wartość dla każdej z nich oraz spróbuj zmienić jej wartość.

# Ciekawostką jest to, że możemy stworzyć „pustą” klasę tylko po to, żeby przechować wartość wielu zmiennych w pojedynczej referencji, coś jak struktura w języku C.

class Pracownik:
    pass #gdy nie ma defow chyba

janek = Pracownik()
janek.imie = "Janek"
janek.nazwisko = "Kowalski"
janek.wiek = 30

print(janek.wiek)
#Wracając do zmiennych prywatnych z zestawu 4 warto jeszcze wiedzieć o sposobie „dostania” się do tej zmiennej.

class Pracownik2:
    __prywatna = "tajne hasło"

    def __init__(self, imie):
        self.imie = imie

janek2 = Pracownik2("Janek")
#print(janek2.__prywatna)    # to nie zadziała
print(janek2._Pracownik2__prywatna)   # ale to już tak