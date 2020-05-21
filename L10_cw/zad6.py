import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
 
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
gr1 = df.groupby(['Plec']).agg({'Liczba':['sum']})
ch = df[df['Plec']=='M'].groupby(['Rok']).agg({'Liczba':['sum']})
d = df[df['Plec']=='K'].groupby(['Rok']).agg({'Liczba':['sum']})
gr3 = df.groupby(['Rok']).agg({'Liczba':['sum']})
w = [int(gr3.values[x]) for x in range(len(gr3.values[:]))]
lata = df['Rok'].unique()

plt.subplot(1, 3, 1) # [gr1.values[0][0],gr1.values[1][0]]
plt.bar(['K','M'],[gr1.values[0][0],gr1.values[1][0]],color=['pink','cyan'])
plt.ylabel('Ilość narodzin (mln)')
plt.xlabel('Płeć')

plt.subplot(1, 3, 2)
plt.plot(lata,ch.values[:], label = 'M')
plt.plot(lata,d.values[:], label = 'K')
plt.legend(loc=4)
plt.xlabel('Rok')
# plt.xticks(lata ,rotation=90) #za ciasno

plt.subplot(1, 3, 3)
plt.bar(lata ,w , label = 'Rok')
plt.show()