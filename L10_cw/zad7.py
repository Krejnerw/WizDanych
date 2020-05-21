import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
 
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

ch = df[df['Plec']=='M'].groupby(['Rok']).agg({'Liczba':['sum']})
d = df[df['Plec']=='K'].groupby(['Rok']).agg({'Liczba':['sum']})
lata = df['Rok'].unique()
wch = [int(ch.values[x]) for x in range(len(ch))]
wd = [int(d.values[x]) for x in range(len(d))]
# print(wch,wd)
plt.bar(lata,wch, color='cyan', label = 'chlopcy')
plt.bar(lata,wd, color='pink', label = 'dziewczyny', bottom = wch)
plt.legend(loc=1)
plt.xlabel('Rok')
plt.xticks(lata ,rotation=90) #za ciasno
plt.show()