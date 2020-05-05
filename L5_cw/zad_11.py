def fib(ile_liczb):
    i=0
    a=0
    b=1
    while i<=ile_liczb:
        if i>ile_liczb:
            raise StopIteration
        yield abs(b-a)
        i+=i
        tmp=a
        a=b-a
        b=tmp

f=fib(3)
for i in range(3):
    print(next(f))
