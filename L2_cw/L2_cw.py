import math as m
#zad1
# a=input("Wpisz zdanie\n")
# print (a.count(" "))

#zad2
# import sys 
# print("Podaj 2 liczby")
# a=sys.stdin.readline()
# a=int(a)
# b=int(sys.stdin.readline())
# # b=int(b)
# print("iloczyn : ", a*b)
# sys.stdout.write('tekst '+str(a*b))
    # vol2
# import sys 
# a,b = int(sys.stdin.readline()),int(sys.stdin.readline())
# print('iloczyn : ' + str(a*b))

#zad3
# == ,!== > < ,>= ,<= ,in ,and ,or

# #zad4
# a = float(input("Podaj liczbe : \n"))
# print('Bezwzgledna twojej liczby to : ', abs(int(a))) # podaje tylko wartosc calkowita

# zad5 a (0,10) oraz a>b lub b>c
# a = int(input("Podaj liczbe 1 : \n"))
# b = int(input("Podaj liczbe 2 : \n"))
# c = int(input("Podaj liczbe 3 : \n"))
# x, y, z = int(input("l1 : ")), int(input("l2 : ")), int(input("l3 : "))

# if a>0 and a<10 :
#     if a>b or b>c:
#         print("tak")
# else:
#     print("nie")

# # zad6
# for i in range(21):
#   if i % 5 == 0 and i!=0:
#     print(i)

# # zad7
# x,y =(int(input("l1 : ")),(int(input("l2 : "))))
# print("L1^2 =",pow(x,2),("L2^2 ="),pow(y,2))

# # zad8
# lista=[]
# i = int(input("ile liczb chcesz dodac : "))
# for x in range(i):
#     a=input("liczba: ")
#     lista.append(a)
# print(lista)

# # zad9
# a=list(input("liczba wielocyfrowa: "))
# print(a)
# wynik=0
# i=0
# while (i !=(len(a))):
#     wynik+=int(a[i])
#     i+=1
# else:
#     print("wynik: ",wynik)

# # zad10
# a = int(input("podaj wysokosc wiezy: "))
# while (a<0 or a>10):
#     print("wybierz liczbe od 0 do 10")
#     a = int(input("podaj wysokosc wiezy: ")) 
# else:
#     for i in range(a):
#         print("A"*(i+1))

# # zad 11
# a = int(input('podaj wysokosc od 3 do 9 : '))
# if(a%2!=0):
#     sr=a//2
#     for j in range(sr+1):
#         for i in range(a):
#             if i in range(sr-j,sr+1+j):
#                 # print(' kropka '+str(j)+str(i),end='')
#                 print('o',end='')
#             else:
#                 print(' ',end='')
#                 # print(' spacja '+str(j)+str(i),end='')
#         print('\n')
#     for j in range(1,a-sr):
#         for i in range(a):
#             if i in range(j,a-j):
#                 # print(' kropka '+str(j)+str(i),end='')
#                 print('o',end='')
#             else:
#                 print(' ',end='')
#                 # print(' spacja '+str(j)+str(i),end='')
#         print('\n')
# else:
#     sr=a//2
#     for j in range(sr+1):
#         for i in range(a):
#             if i in range(sr-1-j,sr+1+j):
#                 # print(' kropka '+str(j)+str(i),end='')
#                 print('o',end='')
#             else:
#                 print(' ',end='')
#                 # print(' spacja '+str(j)+str(i),end='')
#         print('\n')
#     for j in range(1,a-sr):
#         for i in range(a):
#             if i in range(j,a-j):
#                 # print(' kropka '+str(j)+str(i),end='')
#                 print('o',end='')
#             else:
#                 print(' ',end='')
#                 # print(' spacja '+str(j)+str(i),end='')
#         print('\n')

# # zad12
# for i in range(1,11):
#     for j in range(1,11):
#         # print('%(a)d*%(b)d = %(c)d' %{'a':j,'b':i, 'c':i*j},end='   ')
#         # print(str(j)+' * '+str(i)+' = '+str(j*i),end='\t')
#         print(str(j*i),end='\t')
#     print('\n')

# try:
    #     instrukcja
    #     wyjatki:
    #     awaryjne instrukcje
# zad13 przestudiowac inne bledy link w zesz

# zad 14
# x = int(input("Proszę wprowadzić liczbę: "))
# try:
#     print(m.sqrt(x))
# except ValueError:
#     print ("Ups! podana liczba jest ujemna")
# # zad 15 #spr czy jest cyfra jak nie to blad
# while 1:
#     try:
#         x = int(input("Proszę wprowadzić liczbę: "))
#         break
#     except ValueError:
#         print ("Uch! to nie jest poprawna liczba! Spróbuj jeszcze raz...")
