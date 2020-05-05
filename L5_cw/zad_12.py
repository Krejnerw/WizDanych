msc=['Styczen','Luty','Marzec','Kwiecien','Maj','Czerwiec','Lipiec','Sierpien','Wrzesien','Pazdziernika','Listopad','Grudzien']
miesiac=(i for i in msc)
print(miesiac)
for i in range(12):
    print(next(miesiac))

