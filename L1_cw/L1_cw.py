import math as m
# # zad 3
# a = 3 
# print(a)
# a += 1
# print(a)
# a -= 1
# print(a)
# a *= 2
# print(a)
# a //= 1
# print(a)
# a /= 3
# print(a)
# a **= 3
# print(a)
# a %= 5
# print(a)

# # zad 4
# print(pow(math.e,10))
# # a=pow(math.sin(8),2)
# # b=math.log(5+a,math.e)
# # print(pow(b,(1/6)))
# print(pow(math.log(5 + pow(math.sin(8),2),math.e), (1/6)))
# print(math.floor(3.55))
# print(math.ceil(3.55))

# print(math.floor(4.8))
# print(math.ceil(4.8))

# # przyklad 6 
# print('wynik dzial jest rowny a=%(zm)d' % {'zm':12})
# a = 5
# b = 3
# z = 5 - 3
# print('wyn dzial  %(z1)d-%(z2)d=%(z3)d' % {'z1':a, 'z2':b, 'z3':a-b})

# # zad 5
# imie='WERONIKA'
# nazw='KREJNER'
# print ('%(b)s %(a)s' %{'b':imie.capitalize(),'a':nazw.capitalize()})
# print (imie.capitalize()+' '+nazw.capitalize())

# # zad 6
# tekst='leci tekst sb lalalalla la la ale nie zawsze lala la la gra la la skonczona piosnka ta ha ha'
# print(tekst.count('la')) #12

# # zad 7
# tekst='sdfghjk'
# print(tekst[0])
# print(tekst[-1])

# # zad 8
# tekst='leci tekst sb lalalalla la la ale nie zawsze lala la la gra la la skonczona piosnka ta ha ha'
# b=tekst.split()
# print(b)

# zad 9
# nie wiem?


# # zad 10
# filmy=['a','edf','wert','q34tgx','ookjzq','1qwe3','awsed']
# filmy.sort()
# print(filmy)

# # zad 11
# st=[0,m.pi/6,m.pi/4,m.pi/3,m.pi/2,m.pi]
# tcos=[round(m.cos(x),3) for x in st]
# tsin=[round(m.sin(x),3) for x in st]
# ttg=[round(m.tan(x),3) for x in st]
# print('[0, pi/6, pi/4, pi/3, pi/2, pi]')
# print(tcos,tsin,ttg,sep='\n')

# #zad 12
# t='zapisuje bardzo dlugie zdanie co najmniej 5 wyrazow'
# p=t.split()
# print(p)

# zad 13
slownik={'klosz':'Adam K',
         'kapucha':'Kaśka P',
         'szpica':'Monika W',
         'robal':'Karol B',
         'sciana':'Dominik M',
         'pietrucha':'Piotrek P',
         'blondi':'Tomek B',
         'rzep':'Zośka A',
         'sola':'Przemek A',
         'ziolko':'Bartek C',
         'zielony':'Kacperc F',
         }
print(slownik['kapucha'])
print(slownik['ziolko'])
print(slownik['szpica'])

# ad 14 skopiuj slownik do innego slownika
slownik2=slownik.copy()
print(slownik2)
slownik['cos']='cos' # dodaje na samym koncu
slownik['zielony']='cos' # dodaje na samym koncu
print(slownik)
print(slownik2)

# zad 15 pominiete

# zad 16 
# stworz slownik z ulub grami komp. pomysl co moze byc kluczem a co wartoscia w takim slowniku. 
# Policz l elem 
print(len(slownik))