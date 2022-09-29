import requests
from math import floor

def get_vreme(city):
    API_KEY = 'f7c3bd093e8f76b2309eca7f2d6fa68e'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    data = requests.get(url).json()
    calc_temp = int(data['main']['temp']) - 273.15
    temperatura = f'Temperatura in {city} este de {floor(calc_temp)} grade.'
    print(temperatura)

if __name__ == '__main__':
    oras = input('City: ')
    get_vreme(oras)

