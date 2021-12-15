from bs4 import BeautifulSoup
import requests
from random import randint

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
elements = soup.select('.CBarticleTitle')

title_start = []
title_end = []

for element in elements:
    text = element.get_text()
    if text.find("COVID") > 0 or text.find("mirti") > 0:
        continue
    elif text.find(":") > 0: #jeigu suranda dvitaski grazina indexa didesni uz 0
        title_start.append(text.split(':')[0])
        title_end.append(text.split(':')[1])

funny_list = []

for element in title_start:
    #paimame random elementa is title pabaigos
    end = title_end[randint(0, len(title_end)-1)]
    funny_tittle = ':'.join([element, end])
    funny_list.append(funny_tittle)

for el in funny_list:
    print(el)

with open('funny_title2.txt', 'w', encoding='utf-8') as file:
    for el in funny_list:
        file.write(f'{el}.\n')

