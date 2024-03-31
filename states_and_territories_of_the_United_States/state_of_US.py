import requests

from bs4 import BeautifulSoup

import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'

data=requests.get(url)

soup=BeautifulSoup(data.content,'html.parser')

list1=soup.find('table',class_='wikitable')

states=[]
for i in list1.find_all('tr')[2:]:
    states.append(i.find('a').text)
