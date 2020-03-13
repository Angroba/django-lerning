

import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        rya=requests.get(make_url(city), make_parameters() )
 except requests.ConnectionError:
        return '<сетевая ошибка>'
    if rya.status_code == 200:
        return rya.text
    else:
        return '<ошибка на сервере погоды>'

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
