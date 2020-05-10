import pandas as pd
import numpy as numpy
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

gr = (df[(df['Rok']>2012)]).groupby(['Plec']).agg({'Liczba':['sum']})
print(gr)
wykres = gr.plot.pie(y = 'Liczba', autopct='%.2f %%', fontsize=20, figsize=(6, 6))
wykres.legend(['Kobiety','Mężczyźni'])
plt.title('Ilość urodzonych chłopców i dziewczynek w latach 2002-2017')
plt.show()
