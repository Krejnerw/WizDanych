#A={1/x: xc<1,10>}
A=[1/x for x in range(1,11)]
print(A)
#B={1,2,4,8,...,2^10}
B=[2**i for i in range(11)]
print(B)
#C={x:xcB i x podziel przez 4}
C=[x for x in B if x%4==0]
print(C)