#rozkminic wybieranie roku z daty
import datetime as dt
import pandas as pd
import numpy as np 

df=pd.read_csv('zamowienia.csv',header=0,delimiter=';')
print(df)
#listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
p=df.agg({'Sprzedawca':'unique'})
print(p)
#5 najwyższych wartości zamówień
print(df.sort_values(by=['Utarg'],ascending=False).head(5))
#ilość zamówień złożonych przez każdego sprzedawcę
print(df.groupby(['Sprzedawca']).agg({'idZamowienia':'count'}))
#sumę zamówień dla każdego kraju
print(df.groupby(['Kraj']).agg({'idZamowienia':'count'}))
#sumę zamówień dla roku 2005, dla sprzedawców z Polski
print((df[((df['Data zamowienia'].str.contains('2005'))&(df.Kraj=='Polska'))]).groupby(['Sprzedawca']).agg({'idZamowienia':'count'}))
#średnią kwotę zamówienia w 2004 roku,
print((df[(df['Data zamowienia'].str.contains('2004'))]).agg({'Utarg':'mean'}))
#zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
df[df["Data zamowienia"].str.contains("2004")].to_csv('zamówienia_2004.csv',index=False,sep=';')
df[df["Data zamowienia"].str.contains("2005")].to_csv('zamówienia_2005.csv',index=False,sep=';')