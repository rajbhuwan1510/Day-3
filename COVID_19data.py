import requests

url='https://data.covid19india.org/v4/min/timeseries.min.json'
data=requests.get(url)
new=data = data.json()
print(new)
