def n_wyraz(a1,nr_wyrazu,r):
    """oblicza n-ty wyraz ciagu arytmetycznego"""
    return a1+(nr_wyrazu-1)*r

def suma_wyrazow(*elementy):
    """oblicza sume podanych wyrazow"""
    return sum(elementy)/len(elementy)

def n_suma(a1,nr_wyrazu,r):
    """oblicza sume arytmetyczna ze wzoru"""
    return (2*a1+(nr_wyrazu-1))*nr_wyrazu/2

def n_sasiedni(a1,a3,n_wyraz):
    if n_wyraz<2:
        return "blad"
    else:
        return (a1+a3)/2
