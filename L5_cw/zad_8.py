class Samogloski:
    """Iterator zwracajacy tylko elementy bedace samogloskami"""
    def __init__(self,ciag):
        if isinstance(ciag,str):
            self.ciag = ciag
        else:
            self.slowo=str(ciag)
        self.ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        sam="AaEeIiOoUuYy"
        self.ind +=1
        if self.ind > len(self.ciag):
            raise StopIteration
        if self.ciag[self.ind] in sam:
            return self.ciag[self.ind]


k='Abcdefghijklmnoprstuwxyz'
kk=Samogloski(k)
kk.__iter__()
for i in k:
    print(kk.__next__())

