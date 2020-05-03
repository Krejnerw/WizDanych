#przed ostatnie nie pokazuje imion
import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx)

#tam gdzie l. imion była większa niż 1000 w danym roku
print(df[df['Liczba']>1000])

#tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df[df['Imie']=='WERONIKA'])

#sumę wszystkich urodzonych dzieci w całym danym okresie,
# print(sum(df['Rok']))
print(df.agg({'Liczba':['sum']}))

#sumę dzieci urodzonych w latach 2000-2005
print((df[(df['Rok']>=2000)&(df['Rok']<2006)]).agg({'Liczba':['sum']}))
#sumę urodzonych chłopców i dziewczynek,
print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(df.groupby(['Rok','Plec']).max())
print(df.groupby(['Rok','Plec']).agg({'Liczba':'max'}))
#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

print(df.groupby(['Plec', 'Imie']).agg({'Liczba': ['sum']})
        .sort_values(('Liczba', 'sum'), ascending=False).iloc[[0, 1]])