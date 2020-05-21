import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rd

df = pd.read_csv('zamowienia.csv',header=0,delimiter=';')
gr = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})

sprzed = df['Sprzedawca'].unique()
wart = [int(gr.values[x]) for x in range(len(gr.values))]
Explode=[0 for i in range(len(gr.index.values))]
Explode[ wart.index(max(wart)) ]=0.1
ax = plt.subplot()
wedges,texts,autotexts = plt.pie(wart, labels = sprzed, shadow = True,
                                explode = Explode,
                                startangle=45,
                                autopct=lambda pct: "{:.1f}%".format(pct), 
                                textprops=dict(color="black"))
plt.axis(xmax=2)
plt.setp(autotexts, size=10, weight="bold")
ax.annotate('naj sprzedawca',
            xy=(1,-0.5),
            xytext=(1.4,-0.8),
            arrowprops=dict(facecolor='black'))
plt.title("Sumy zamowien sprzedawcow")
plt.legend(loc='upper right',title='Sprzedawcy')
plt.show()