# #info git 4_wprowadzenie
# #operacje na plikach
# #poprzez open wbudowana 
# plik= open(nazwa,[tryb[,bufor]])#nazwa jako sciezka
# #tryby 
# # r -odczyt, musi istniec
# # w -zapis if nie ma zostanie utworzony
# # a -dopisywanie, dopisuje na koncu pliku
# # r+ -odcz+zapis, if nie ist tworzy
# # w+ 
# # a+

# . - biezacy folder
# .. - folder nadrzedny
# #change directory
# cd ../../ # 2 poziomy wyzej w strukturze
# cd c:\windows\system32
# cd /usr/bin #unix linux?
# cd ../folder
# cd usr/../folder #podglad gdzie sie jest?

# import os.path

# plik = open(r'sciezka do pliku')
# zadanie= 'ostatnio czyt \'costam\''
# r=raw

# w+ odczyt i zapis if plik nie ist zost utworz
# #najpierw all usunie a potem zapisze

# read() #-> pusty string
# write('linia')
# read() #-> pusty string

# linia w pliku

# plik.seek(0, 0)
# readline() -> string 'linia w pliku'
# read([rozmiar])#-bez podania rozmiaru mg byc problemy
# readline([rozmiar]) #bez podania rozmiaru bd wczytywac po lini
# readlines() #zwraca liste wierszy

# write(lancuch)#musi byc string
# writelines(lista)#kazdy elem w nowym wierszu

# przyklad 3 zalecany sposob czegos(odczytu/zapisu) tam plikow
# with #zwalnia z obowiazku zamyk pliku--niejawny close
# ale poza petla nie obsluzymy pliku bo bd zamknieta

# liczba =5
# imie = 'ja'
# print(type(imie))
# print(type(liczba))

# <class 'str'>
# <class 'int'>
# dziedziczenie i interfejsy sa lepsze niz dziedziczenie jakies tambo nie posiada interfejsow

#przyklad do garbage collector
imie = 'ja'
ime2=imie #pamieta przestrzen w pamieci zm imie
print(id(imie))
print(id(imie2))
#bd ta sama wartosc

imie = 'ja'
ime2=imie #pamieta przestrzen w pamieci zm imie
imie ='ty' #zmienia odniesienie w pamieci
print(id(imie))
print(id(imie2))
#bd rozna wartosc

imie = 'ja'
#ime2=imie #pamieta przestrzen w pamieci zm imie
imie ='ty' #zmienia odniesienie w pamieci
#print(id(imie2))
imie =[z for z in range(1 ,1000)]
print(id(imie))
#bd ta sama wartosc
#przeanalizowac zad 8