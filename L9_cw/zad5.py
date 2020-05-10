import datetime as dt
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv',header=0,delimiter=';')
print(df)
gr = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
wykres = gr.plot.bar()
wykres.set_xlabel('Sprzedawca')
wykres.legend(['Liczba zamowień'])
plt.title('Suma zamównień dla sprzedawcy')
plt.show()