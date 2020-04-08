#komprechencje --> jednolinijkowce tworzace liste
#zamiast pisać w pętli
# lista = []
# for element in zakres:
#     if jakis_war(element):
#         lista.append("cos sie dzieje z: "+ element)

# #mozna
# lista = ["cos sie dzieje z: "+ element for element in zakres if jakis_war(element)]

[printf(f"liczba: {X}")for x in range(5)]
print(type([print(f"liczba: {x}")for x in range(5)]))
print(len([print(f"liczba: {x}")for x in range(5)]))

# lista = []
# for x in range(5):
#     if x%2==0:
#         lista.append(x)
    
## pakiet timeit
#[x for x in range(5) if x%2==0]
    #to samo co powyzsze w 1 linijce
#slowniki i zamiana klucza z wartoscia

slownik = {'imie': 'Adam', 'wiek': 28}

for cos in slownik: #slownik.keys()
    print(cos)

for cos in slownik.values():
    print(cos)

for cos in slownik.items():
    print(cos)

krotka = tuple(['Marek', 23])
krotka = ('Marek', 23)

krotka[1] = 24 
#nie zmieni sie bo krotka jest nie mutowalna
krotka = ('Marek', 24) 
#przypisanie calkowicie nowej krotki w msc starej

for klucz, wartosc in slownik.items:
    print(cos)

('imie', 'Adam')
('wiek', 28)

#funkcje
def nazwa_f(arg_pozycyjne, arg_domyslny=wartosc, *arg_4, **arg_5):
    instrukcje
    return wartosc

#np str net
#np za zad 8 i 9

#pakiet math/plik math

#symb * oznacza dowolna ilosc arg przechowywanych w krotce
def ciag(* liczby):
    if len(liczby)==0:
        return 0.0
    else:
        suma = 0.0
        #sumujemy elementy ciagu
        for i in liczby:
            suma+=i
        #zwracamy wartosc sumy
        return suma
#wywol gdy brak elementow
print(ciag())
print(ciag(1,2,3,4,5,6))

import test
test.cos_co_tam_jest
#tworzenie pakietu nazwa__init__.py
#i tam powsadzac importy jakies

def dluga_nazwa_waznej_funkcji(imie):
    print(d'elo {imie}! XD')

short = dluga_nazwa_waznej_funkcji
print(short)
print(type(short))

short('Ja')