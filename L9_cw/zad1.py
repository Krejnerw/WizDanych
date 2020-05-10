import pandas as pd
import numpy as numpy
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

gr = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(gr)
wykres = gr.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Rok')
wykres.legend(['Liczba'])
plt.title('Liczba narodzin na każdy rok')
plt.show()
