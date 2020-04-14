def monotonicznosc(a):
    if a>0:
        print("f.rosnaca")
    elif a<0:
        print("f.malejaca")
    else:
        print("f.stala")
        
n=int(input("podaj a: "))
monotonicznosc(n)