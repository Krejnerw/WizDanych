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
        return self.x,self.y

    def __del__(self):
        return


postac=Robaczek(0,0,2)
postac.idz_w_dol(5)
postac.idz_w_lewo(2)
print(postac.pokaz_gdzie_jestes())
postac.__del__()
#del postac
print(postac.pokaz_gdzie_jestes())