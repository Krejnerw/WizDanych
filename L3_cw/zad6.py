from math import sqrt,pow
def dl_r(x=0,y=0,a=0,b=0):
    return sqrt(pow(x-a,2)+pow(y-b,2))
print(dl_r(4,5,8,5))
print(dl_r(1))


