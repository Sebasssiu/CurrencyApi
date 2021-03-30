import requests
from bs4 import BeautifulSoup
from decimal import Decimal

"""
Desc: this function scrapes banguat 
website in seek of currency exchange for a 
particular coin in a particular date.
@params
date: date of currency exchange rate format= YYYY-MM-DD
currency: the evaluated coin either USD or EU
"""


def exchange_rate(date, currency):
    date = date.split("-")
    URL = f'https://www.banguat.gob.gt/cambio/historico.asp?ktipo=3&kdia={date[2]}&kmes={date[1]}&kanio={date[0]}&submit1=Consultar'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    html_elements = soup.findAll('tr')
    currency = 'DólaresdeEE.UU.**' if currency == 'USD' else 'Euro'
    for position in range(len(html_elements)):
        currency_data = html_elements[position].text.split('\n')
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


"""
Desc: this function compares values from banguat
and is gonna return the mean, max value and min value
from a given currency in 2 different dates
@params
date1: date of currency exchange rate format= MM-DD-YYYY
date2: date of currency exchange rate format= MM-DD-YYYY
currency: the evaluated coin either USD or EU
"""


def exchange_rate_comparison(date1, date2, currency):
    currency_rate_date1 = exchange_rate(date1, currency)
    currency_rate_date2 = exchange_rate(date2, currency)
    if currency_rate_date1['coin'] != 'NaN' and currency_rate_date2['coin'] != 'NaN':
        sum_currency_rate = Decimal(currency_rate_date1['exchangeRate']) + Decimal(currency_rate_date2['exchangeRate'])
        mean_currency_rate = sum_currency_rate / 2
        return {
            'mean': mean_currency_rate,
            'max': max(Decimal(currency_rate_date1['exchangeRate']), Decimal(currency_rate_date2['exchangeRate'])),
            'min': min(Decimal(currency_rate_date1['exchangeRate']), Decimal(currency_rate_date2['exchangeRate']))
        }
    return {
        'mean': 'NaN',
        'max': 'NaN',
        'min': 'NaN'
    }