import requests
from bs4 import BeautifulSoup
from decimal import Decimal

"""
Desc: this function will scrape banguat 
website in seek of currency exchange for a 
particular coin in a particular date.
@params
date: date of currency exchange rate format= MM-DD-YYYY
currency: the evaluated coin either USD or EU
"""
def exchange_rate(date, currency):
    date = date.split("-")
    URL = f'https://www.banguat.gob.gt/cambio/historico.asp?ktipo=3&kdia={date[1]}&kmes={date[0]}&kanio={date[2]}&submit1=Consultar'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    html_elements = soup.findAll('tr')
    for position in range(len(html_elements)):
        currency_data = html_elements[position].text.split('\n')
        currency = 'DólaresdeEE.UU.**' if currency == 'USD' else 'Euro'
        if len(currency_data) == 4 and currency_data[1].replace(' ', '') == currency:
            response = {
                'coin': currency_data[1],
                'exchangeRate': currency_data[2]
            }
            return response
    return {
                'coin': 'NaN',
                'exchangeRate': 'NaN'
            }