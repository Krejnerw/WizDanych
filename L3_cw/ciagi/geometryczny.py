import math as m
def n_wyraz(a1,n_wyraz,q):
    if n_wyraz<2:
        return "blad"
    else:
        return a1*q**(n_wyraz-1)

def n_suma(**elementy):
    """oblicza sume podanych wyrazow"""
    return sum(elementy)/len(elementy)

def n_suma(a1,n_wyraz,q):
    if q==1:
        return n_wyraz*a1
    else:
        a1*(1-q**n_wyraz)/(1-q)

def n_sasiedni(a1,a3,n_wyraz):
    if n_wyraz<2:
        return "blad"
    else:
        return m.sqrt(a1*a3)