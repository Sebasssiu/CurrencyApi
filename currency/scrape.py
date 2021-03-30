import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
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
    date1 = date1.split("-")
    date2 = date2.split("-")
    date_start = date(int(date1[0]), int(date1[1]), int(date1[2]))
    date_end = date(int(date2[0]), int(date2[1]), int(date2[2]))
    days = (date_end - date_start).days
    currency_sum = 0
    min_value = max_value = Decimal(exchange_rate(str(date_start), currency)['exchangeRate'])
    for i in range(days):
        actual_currency_rate = exchange_rate(str(date_start), currency)['exchangeRate']
        if actual_currency_rate != 'NaN':
            actual_currency_rate = Decimal(actual_currency_rate)
            currency_sum += actual_currency_rate
            max_value = max(actual_currency_rate, max_value)
            min_value = min(actual_currency_rate, min_value)
        date_start += timedelta(days=1)
    return {
        'mean': currency_sum/days,
        'min': min_value,
        'max': max_value
    }
