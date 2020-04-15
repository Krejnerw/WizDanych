class NaZakupy:

    # definicja konstruktora
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        #deklarujemy atrybuty
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
        #self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        
    def wyswietl_produkt(self):
        return self.nazwa_produktu,self.ilosc,self.jednostka_miary,self.cena_jed

    def ile_produkty(self):
        return self.ilosc, self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed


lista=NaZakupy("marchew",2,"sztuki",3)
print(lista.wyswietl_produkt())
print(lista.ile_kosztuje())