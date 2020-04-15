class Robaczek:

    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok

    def idz_w_gore(self,ile_krokow):
        self.y+=ile_krokow*self.krok

    def idz_w_dol(self,ile_krokow):
        self.y-=ile_krokow*self.krok

    def idz_w_lewo(self,ile_krokow):
        self.x-=ile_krokow*self.krok

    def idz_w_prawo(self,ile_krokow):
        self.x+=ile_krokow*self.krok

    def pokaz_gdzie_jestes(self):
        print("X:",self.x,"Y:",self.y) 

    def __del__(self):
        del self.x
        del self.y
        del self.krok
        print("postac umiera")


postac=Robaczek(0,0,2)
postac.idz_w_dol(5)
postac.idz_w_lewo(2)
postac.pokaz_gdzie_jestes()
postac="To"
