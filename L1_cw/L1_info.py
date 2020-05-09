#typy danych
    #pojedyncza linia
str1 = 'ale kot'
str3 = "ale kot"
print(str1, str3,sep= ", ", end ="\n")
str2 = """ala
ma 
duzego 
kota"""
str4 = 'ala\nma\nduzego\nkota'
print(str2, str4,sep= ", ", end ="\n")
#Jak zapisać w stringu: Wielokrotnie oglądałem film "Sami swoi". ?
#Są przynajmniej dwie możliwości:
s1 = 'Wielokrotnie oglądałem film "Sami swoi".'
s2 = "Wielokrotnie oglądałem film \"Sami swoi\"."
#backslash uzyj \\.
print ( s1[0], s1[2], s1[-1], s1[-2], len(s1), sep= ", ", end ="\n")
print (s1[1:4], s1[0:4], s1[:4], s1[7:] +"\n"+ s1[::2], s1[::-1], sep= ", ", end ="\n")

print(chr(65),chr(97)) #zamieni na litery w kodzie ASCII
print(ord("a"),ord("A")) #wypisze kod litery w ASCII

#Powiedzmy, że 
s = "kosa"  
#Chcemy drugi znak zmienić na 'a'.  
#s[1] = 'a'  nie zadziała.
#Stringi w Pythonie są niemutowalne (niezmienne).
s = s[0] + 'a' + s[2:]
print(s)

#Oto przykłady metod, które możemy wywołać dla napisu s:
s.capitalize() # zwraca napis ze zmienioną pierwszą literą na wielką
s.isdigit() # sprawdza, czy wszystkie znaki są cyframi
s.islower() # sprawdza, czy wszystkie litery są małe
s.center(długość) # centruje napis w polu o podanej długości 
                  # (uzupełniając spacjami)
s.rjust(długość) # wyrównuje do prawej w polu o podanej długości 
                 # (uzupełniając spacjami)
s.count(s1) # zlicza wystąpienia podciągu s1 w s
s.lstrip() # zwraca napis z usuniętymi wiodącymi białymi znakami
    # Podkreślmy: funkcje te nie zmieniają s!  
    # Np. s.center(...) zwraca nowy napis.  
    # Przypominamy też wielce użyteczną funkcję len(s) 
    # (wykorzystywana w Pythonie do rozmaitych kolekcji, 
    # nie tylko stringów).

a = 123
b = 12.45
c = 12 +15j
print(int(a) , float(b), complex(c), sep= ", ", end ="\n")#to raczej niekonieczne
print( a, b, c, sep= ", ", end ="\n")

del c #usuwa zmienne c jako nazwa zmiennej
print(id(a)) #drukuje adres zmiennej

#dzialania 
print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5//5) # dzielenie bez reszty
print(5%5) # modulo
print(5**5) # potegowanie
print(pow(3,2))

print (type(b)) #pod tekstem jest zmienna lub "cos" lub liczby

#Deklaracja wielokrotna
zm1, zm2, zm3, zm4 = 1, 2, 3, 4
#operatory przyrostkowe 
a = 3 
a += 1

print("ALA ma"+"kotow") # konkatencja

print("ALA ma" + str(5) + " kotow")
liczba=int("100")

print("Ala "* 10)

# listy sa mutowalne

lista = []
print(type(lista))

lista2= [1,2,3]
print(lista2[0])
imie="maggi"
print(imie[0])
lista2[0]= 5
imie ="pupi"

imie.swapcase() #male na duze duze na male ale nie w stringu
print(imie) #bd bez zmian
print(imie.swapcase())
imie=imie.swapcase()
print(imie)
"Ala".swapcase()
lista2.append(1) #dodaje element na koniec listy

lista3= [1,"ala", 4.5,None,True, [1,2]] #sortowanie nie wywyzsza zadnego typu
lista3[5][1]

#import biblioteki matematycznej
from math import *
a = 0.264
print(round(a))
print(pi)
print(sin(2))
print(sqrt(9))

macierz = [
 [1,2,3],
  [4,5,6],
  [7,8,9]
  ]
macierz [1][1] #5
nowa =lista2 + macierz 

#slownik 
slownik = {}
slownik ['imie'] = 'Adam'
slownik [0]= 'Adam'
print (slownik)
slownik2 = {'imie': 'Adam', 0 : 'Adam'}
print(slownik2.keys())
print(slownik2.values())

#A dictionary can also contain many dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Or, if you want to nest three dictionaries that already exists as dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#It is also possible to use the dict() constructor to make a new dictionary:

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)