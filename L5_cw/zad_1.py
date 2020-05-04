class Material:
    
    def __init__(self,r,d,s):
        self.rodzaj=r
        self.dlugosc=d
        self.szerokosc=s

    def wyswietl_nazwe(self):
        print("Material: ",self.rodzaj)
        #return "{}".format(self.rodzaj)

class Ubrania(Material):
    def __init__(self,r,k,d):
        self.rozmiar=r
        self.kolor=k
        self.dla_kogo=d

    def wyswietl_dane(self):
        #return self.rozmiar, self.kolor, self.dla_kogo
        print("Ubranie: ",self.rozmiar, self.kolor, self.dla_kogo)
        #return "{}, {}, {}".format(self.kolor, self.dla_kogo, self.rozmiar)


class Sweter(Ubrania):

    def __init__(self,r):
        self.rodzaj_swetra=r

    def wyswietl_dane(self):
        #return self.rodzaj_swetra
        print("Sweter: ",self.rodzaj_swetra)


ob1=Material("rodzaj",20, 50)
ob1.wyswietl_nazwe()

ob2=Ubrania("rozmiar","kolor","fur")
#ob2.wyswietl_nazwe()
ob2.wyswietl_dane()

ob3=Sweter("rodzaj_s")
#ob3.wyswietl_nazwe()
ob3.wyswietl_dane()
