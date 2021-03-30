import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
from decimal import Decimal
import threading

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
    if currency == 'USD':
        rate = soup.find(string=" Dólares de EE.UU. **").find_next('td').contents[0].contents[0]
        return {
            'coin': currency,
            'exchangeRate': rate
        }
    rate = soup.find(string=" Euro ").find_next('td').contents[0]
    return {
            'coin': currency,
            'exchangeRate': rate
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
    moneda = '02' if currency == 'USD' else '24'
    URL = f'https://www.banguat.gob.gt/cambio/historico.asp?kmoneda={moneda}&ktipo=5&kdia={date1[2]}&kmes={date1[1]}&kanio={date1[0]}&kdia1={date2[2]}&kmes1={date2[1]}&kanio1={date2[0]}&submit1=Consultar'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    html_elements = soup.find_all('td', {'class': 'mitexto', 'colspan': None})
    mean = 0
    max_value = min_value = Decimal(soup.find('td', {'class': 'mitexto'}).find_next('td', {'class', 'coltexto'}).contents[0])
    for r in html_elements:
        rate = Decimal(r.find_next('td', {'class', 'coltexto'}).contents[0])
        mean += rate
        max_value = max(max_value, rate)
        min_value = min(min_value, rate)

    return {
        'mean': mean/len(html_elements),
        'min': min_value,
        'max': max_value
    }



