#Listing 1 – tworzenie Series i DataFrames
import pandas as pd
import numpy as np

# Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])#np.nan=None
#gdy jest none to zmienne jako float64
print(s)
s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Eleonora'])
print(s)

# DataFrame
# tworzenie dataframe na podstawie słownika
data = {'Kraj': ['Belgia',  'Indie',  'Brazylia'],
'Stolica': ['Bruksela',  'New Delhi',  'Brasilia'],
'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data,columns=['Kraj',  'Stolica',  'Populacja'])
# wystarczy tak w tym przypadku
# df = pd.DataFrame(data)
print(df)
# DataFrame przechowuje typ dla każdej kolumny co możemy sprawdzić wypisując
print(df.dtypes)
# możemy również w prosty sposób stworzyć serię danych - czyli próbki dla kolejnych
# dat, pomiarów czasu
daty = pd.date_range('20180401', periods=5,freq='M')#zobaczyc frequency
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)
#randn-liczby z rozkladu normalnego czy cos
#randn(5,4)-dwa wymiary
#randn((5,4))-1 wymiar 2 elem

# biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
# CSV, odczyt i zapis
df = pd.read_csv('dane.csv', header=None, nrows=2)#nrows ile ma pobrac linijek
#modified
df = pd.read_csv('dane.csv', header=0,delimiter=';')
print(df)
df.to_csv('plik.csv', header=None, index=False)
#header etykiety tak czy nie
#plik w next lekcji

# Excel - wymagana bibioteka xlrd oraz openpyxl
import xlrd
import openpyxl
#trzeba zainstalowac

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
df2 = pd.read_excel(xlsx)
print(df)
df = pd.read_excel(xlsx,'Arkusz2') #'sheet name'
print(df)
df2.to_excel('calosc.xlsx')
df2.to_excel('bez_cos.xlsx', sheet_name='Arkusz1')
df2.to_excel('z_cos.xlsx',  sheet_name='Arkusz2')
#nie tak jak chce jeszcze do ogarniecia


# biblioteka Pandas może również dzięki bibliotece sqlalchemy odczytywać
# dane bezpośrednio z baz danych, lub zapisywać je do SQL-a
# ten temat wykracza jednak poza zakres aktualnej lekcji i może
# zostanie zaprezentowany w lekcji polegającej na wyświetlaniu wykresów na postawie
# danych pochodzących z plików i zewnętrznych źródeł