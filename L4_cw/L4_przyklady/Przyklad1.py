# 1.Otwarcie pliku

# plik = open(nazwa, [tryb[, bufor]])

# plik – nazwa obiektu, którą sami nadajemy
# nazwa – nazwa pliku na dysku, jaka jest
# tryb – tryb otwarcia pliku (np. do odczytu, do zapisu itd.)
# bufor – obszar pamięci przechowujący dane w oczekiwaniu na zapis i odczyt

#2.Odczytanie danych z pliku:

# można użyć komend:

# read([rozmiar]) - odczytuje dane o rozmiarze, jeśli podany
# readline([rozmiar]) – odczytuje wiersz lub ilość znaków jeśli podano rozmiar
# readlines() – odczytuje wiersze z pliku

plik = open("dane.txt","r")

#odczyt 10 znaków z pliku
znaki = plik.read(10)

#odczyt jednej lini z pliku--od 10 miejsca
linia = plik.readline()

#odczyt wierszy z pliku--od momentu skonczonej linijki
wiersze = plik.readlines()

#zamkniecie pliku
plik.close()
#drukujemy 10 znakow

print(znaki)
print("\n")
#drukujemy linię

print(linia)
print("\n")
#drukujemy cały plik

print(wiersze)
print("\n")