class ciagi:

    a1=0
    r=0
    n=0

    def wyswietl_dane(self):
        return self.a1, self.r, self.n

    def pobierz_elementy(self,*elementy):
        self.a1=elementy[0]
        self.elementy=elementy

    def pobierz_parametry(self,a1,r,n):
        self.a1=a1
        self.r=r
        self.n=n

    def policz_sume(self):
        if self.n!=0:
            return ((((2*self.a1+((self.n-1)*self.r))*0.5))*self.n)
        return sum(self.elementy)
    #???
    def policz_elementy(self):
        if self.n!=0:
            lista = [self.a1+self.r*i for i in range(self.n)]
            return lista
        return [self.elementy[i]for i in range(len(self.elementy))]
            
        

ciag = ciagi()

print(ciag.wyswietl_dane())
ciag.pobierz_elementy(1.5,2.5,3.5)
print(ciag.policz_elementy())
print(ciag.policz_sume())
ciag.pobierz_parametry(1.5,1,3)
print(ciag.policz_elementy())
print(ciag.policz_sume())
print(ciag.wyswietl_dane())