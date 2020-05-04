class Material:
    rodzaj=""
    dlugosc=0
    szerokosc=0
    def __init__(self,r,d,s):
        self.rodzaj=r
        self.dlugosc=d
        self.szerokosc=s

    def getinfoM(self,r,d,s):
        """pozwalapobrac informacje o materiale"""
        self.rodzaj=r
        self.dlugosc=d
        self.szerokosc=s

    def wyswietl_nazwe(self):
        # print("Material: ",self.rodzaj)
        #return "{}".format(self.rodzaj)
        print(self.__class__.__name__)

class Ubrania(Material):
    rozmiar=""
    kolor=""
    dla_kogo=""
    def __init__(self,r,k,d):
        self.rozmiar=r
        self.kolor=k
        self.dla_kogo=d

    def getinfoU(self,r,k,d):
        """pozwalapobrac informacje o ubraniu"""
        self.rozmiar=r
        self.kolor=k
        self.dla_kogo=d

    def wyswietl_dane(self):
        #return self.rozmiar, self.kolor, self.dla_kogo
        # print("Ubranie: ",self.rozmiar, self.kolor, self.dla_kogo)
        #return "{}, {}, {}".format(self.kolor, self.dla_kogo, self.rozmiar)
        print("{} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo))

class Sweter(Ubrania):
    rodzaj_swetra=""
    def __init__(self,r):
        self.rodzaj_swetra=r

    def getinfoS(self,r):
        """pozwalapobrac informacje o swetrze"""
        self.rodzaj_swetra=r

    def wyswietl_dane(self):
        #return self.rodzaj_swetra
        # print("Sweter: ",self.rodzaj_swetra)
        print("{} {} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj_swetra))


ob1=Material("rodzaj",20, 50)
ob1.wyswietl_nazwe()

ob2=Ubrania("rozmiar","kolor","fur")
#ob2.wyswietl_nazwe()
ob2.getinfoM('bawelna',50,75)
ob2.wyswietl_dane()

ob3=Sweter("rodzaj_s")
#ob3.wyswietl_nazwe()
ob3.getinfoM('poliester',120,60)
ob3.getinfoU('M','czarny','Pani M.')
ob3.wyswietl_dane()
