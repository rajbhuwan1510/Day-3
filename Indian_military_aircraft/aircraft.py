import requests
import pandas as pd
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft'
data=requests.get(url)

soup=BeautifulSoup(data.content,'html.parser')
list1=soup.find('table',class_='wikitable')

for i in list1.find_all('tr')[2:]:
  try:
    print(i.find('td').text)
  except:
    continue
