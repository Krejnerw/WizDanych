print("HI costam")
tekst="hi there"
tekst='hi there'
tekst="""hi 
there"""
print(tekst)

 #tekst =0

print (type(tekst))
print (type(5))
print (type(5.5)) # uzywac kropki
print (type(True))
print (type(None))
#komentarz : spr typu zm.
print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5//5) # dzielenie bez reszty
print(5%5) # modulo
print(5**5) # potegowanie

print("ALA ma"+"kotow") # konkatencja

print("ALA ma" + str(5) + " kotow")
liczba=int("100")

print("Ala "* 10)

# listy sa mutowalne
#nie dziala ale nwm co

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

def pow():
    pass

# for element in kolekcja:
from math import *
import math as mis
from math import pow
mis.pow(2,2)