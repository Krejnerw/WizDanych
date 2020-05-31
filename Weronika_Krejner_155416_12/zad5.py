from bs4 import BeautifulSoup
import urllib3
import pandas as pd

def gry_slownik(url):
    gry={
            'tytul':[],
            'platforma':[],
            'data wydania':[],
            'ocena':[]
        }
    soup=BeautifulSoup(http.request('GET',url).data,'lxml')
    for x in soup.find_all('table'):
        for y in x.find_all('td',{'class':'clamp-summary-wrap'}):
            gry['tytul'].append(y.find('h3').string.strip())
            for z in y.find_all('div'):
                if z['class'] == ['clamp-score-wrap']:
                    gry['ocena'].append(int(z.find('div').string.strip()))
                elif z['class'] == ['clamp-details']:
                    gry['platforma'].append(z.find('span',{'class':'data'}).string.strip())
                    gry['data wydania'].append(z.find('span',{'class':None}).string)
    return gry

url = 'https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page='
adresy = [url+str(i) for i in range(1,10)]
http = urllib3.PoolManager()
page = http.request("GET", url+'0')

df=pd.DataFrame(gry_slownik(url))
print(df)

for i in adresy:
    gry = gry_slownik(i)
    df = df.append(pd.DataFrame(gry),ignore_index=True)
print(df.where(df['platforma']=='PC').sort_values('ocena',ascending=False).head(10))
