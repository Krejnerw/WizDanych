lista = []
plik = open("Zad1.txt","a+")
for i in range(100):
    if i%4==0:
        lista += [i]
        #plik.write(str(i))
plik.writelines(str(lista))

plik.close()
