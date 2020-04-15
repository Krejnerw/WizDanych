tekst=open("dane.txt", "r")
with open("Zad3.txt", "a+") as plik:
    for linia in range(5):
        l = tekst.readline()
        plik.writelines(l)
        #print(l, end="")
with open("Zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
