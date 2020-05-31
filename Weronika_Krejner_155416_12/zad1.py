# nwm jak to ma byc

#Ze strony https://boardgamegeek.com pobierz linki (znajdź odpowiednie atrybuty) z sekcji 'Announcements'. Wyświetl te linki.
from lxml import html
import requests

url = "https://boardgamegeek.com"
data = requests.get(url)
page = html.fromstring(data.text)

# div_block = '//*[@class="media-module ng-scope"]'
xpath = '//*[@id="results_1"]//div//div//div[2]//div[2]//h2'
# xpath = '//*[@id="results_1"]/*[@class="stretched-link link-text-color"]'
table_div = page.get_element_by_id('results_1')
table = table_div.xpath('./div/div/div[2]/div[2]/h2')[0]
# //*[@id="results_1"]/div/div/div[2]/div[2]/h2/a
print(table)
# xpath = '//*[@id="results_1"]//*[@class="media-relative ng-scope"]//h2//href'
# xpath = '//*[@class="media-cell__title"]//a'
# # -------------do id -----------------------------
# linki = [label for label in page.xpath('.//h2')]
linki = [label for label in table.xpath('.//a')]
print(linki)
labels = []
for i in linki:
    link = i.xpath('./a/href')
    # link = i.get('href')
    # print(link)
    if len(link) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        labels.append(link[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        labels.append(i.text.strip())
print(labels)

