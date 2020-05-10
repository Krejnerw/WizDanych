import pandas as pd
import numpy as numpy
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
gr = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(gr)
wykres = gr.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Pleć')
wykres.legend(['Liczba'])
plt.title('Liczba urodzen z podzialem na plec')
plt.show()