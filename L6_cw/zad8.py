# Napisz funkcję, która:

# -jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy 
        # oraz parametr ‘kierunek’,
# -parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie 
        # czy poziomie
# -funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli 
# komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, 
# nie pozwala na operację)
import numpy as np

def f(tab,kierunek):
        podzial=True
        if kierunek=="pion":
                if int(tab.shape[1]%2==0):
                        wym=int(tab.shape[1]/2)
                        t1=tab[:,:wym]
                        t2=tab[:,wym:]
                else:
                        podzial=False
        elif kierunek=="poziom":
                if int(tab.shape[0]%2==0):
                        wym=int(tab.shape[0]/2)
                        t1=tab[:wym,:]
                        t2=tab[wym:,:]
                else:
                        podzial=False
        else:
                return "bledna zmienna"
        if podzial==True:
                # return 'tablice po podziale:{}\n{}'.format(t1,t2)
                return t1,t2
        else:
                return "nie mozna podzielic"


a=np.array([[x for x in range(5)] for i in range(5)])
print(f(a,"pion"))
print(f(a,"poziom"))
b=np.array([[x for x in range(6)] for i in range(6)])
print(f(b,"pion"))
print(f(b,"poziom"))
