import math
def dl_przeciwprost(a=0,b=0):
    if a==0 or b==0:
        return 0
    else:
        return math.sqrt(a**2+b**2)
        
print(dl_przeciwprost(3,4))
print(dl_przeciwprost(3))