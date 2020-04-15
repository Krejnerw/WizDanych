class Slowa:
    slowo1=""
    slowo2=""

    def podaj_2_slowa(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2

    def sprawdz_czy_palindrom(self):
        if self.slowo1 == "".join(reversed(self.slowo1)):
            return 1
        else:
            return 0

    def sprawdz_czy_metagramy(self):
        n=0
        for i in range(len(self.slowo1)):
            if self.slowo1[i]!=self.slowo2[i]:
                n+=1        
        if n==1:
            return 1
        else:
            return 0

    def sprawdz_czy_anagramy(self):
        for i in range(len(self.slowo1)):
            litera=self.slowo1[i]
            n=0
            for j in range(len(self.slowo2)):
                if litera==self.slowo2[j]:
                    n+=1
            if n==0:
                return 0
        return 1

    def wyswietl_wyrazy(self):
        return self.slowo1,self.slowo2


obiekt = Slowa()
obiekt.podaj_2_slowa("mata","tama")
print(obiekt.wyswietl_wyrazy())
print(obiekt.sprawdz_czy_palindrom())
print(obiekt.sprawdz_czy_metagramy())
print(obiekt.sprawdz_czy_anagramy())
obiekt.podaj_2_slowa("kajak","")
print(obiekt.wyswietl_wyrazy())
print(obiekt.sprawdz_czy_palindrom())
obiekt.podaj_2_slowa("mata","tata")
print(obiekt.wyswietl_wyrazy())
print(obiekt.sprawdz_czy_metagramy())