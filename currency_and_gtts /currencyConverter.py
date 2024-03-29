#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_SGNHumnvIhlNoFUIcLQnkgLeZgTH8TfALAY6kGp3'
BASE_URL = 'https://open.er-api.com/v6/latest/'

def convert_currency(from_currency, to_currency, amount):
    url = f'{BASE_URL}{from_currency.upper()}'
    params = {'apikey': API_KEY, 'symbols': to_currency.upper()}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'error' in data:
        print(f'Error: {data["error"]["message"]}')
        return None
    
    if to_currency.upper() not in data['rates']:
        print(f'Error: Currency code "{to_currency}" not found')
        return None
    
    rate = data['rates'][to_currency.upper()]
    converted_amount = amount * rate
    return converted_amount

# Example usage
from_currency = input("from which currency:")
to_currency = input("to which currency:")
amount = int(input("enter ammount:"))
converted_amount = convert_currency(from_currency, to_currency, amount)
print(f'{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}')

