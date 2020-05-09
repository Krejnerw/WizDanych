# if liczba in[1 ,2 ,2,3] #czy liczba jest w kolekcji
#     print(liczba)
# else:
#     print(liczba)

# for liczba [1,2,3,10]:
#     print(liczba)

# for litera in imie:
#     print(litera)

# for liczba in range(5):
#     #start,stop ,step 3 opcje bycia range() start obowiazkowe/generuje cos
#     print(liczba)

#for liczba in range(5,)...
lista=['a','b',3,5,'to']
for index in range(len(lista)):
    print(index) 
            # 0
            # 1
            # 2
            # 3
            # 4
for index, element in enumerate(lista,start=0):
    print(f'wiersz {index}:{element}')
    #index,element =(1,1) rozpakowanie
    #krotka, ang. tuple, np, (indeks,element)
            # wiersz 0:a
            # wiersz 1:b
            # wiersz 2:3
            # wiersz 3:5
            # wiersz 4:to

    # try:
    #     instrukcja
    #     wyjatki:
    #     awaryjne instrukcje

a,b=input(),input()
print(a,b)

a,b=int(input()), int(input())
print(a,b)