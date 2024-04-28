'''
This program 
'''

import requests

API_KEY = '' # signup and get API_KEY from freecurrencyapi.com
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['EUR', 'USD', 'CAD']

def convert_currency(base):
    currencies = ",".join(CURRENCIES) # convert the array of currencies into a string seperated comma
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}" # here, we build the url for the request

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency")
        return None

while True:
    base_currency = input("Enter the currency you want to convert to (q for quit): ").upper()

    if base_currency == 'Q':
      break

    d = convert_currency(base_currency)

    if not d:
        continue

    for ticker, value in d.items():
       print(f'{ticker}: {value}')