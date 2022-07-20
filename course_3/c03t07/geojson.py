# Обращение к учебному API, имитирующему API Google Maps
# http://py4e-data.dr-chuck.net/json? (key = 42, adress = str)
# API возвращает JSON, после парсинга которого извлекается place_id
# Тестовый адрес: South Federal University
# Контрольный адрес: R V College of Engineering

import urllib.request, urllib.parse, urllib.error
import json

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

# Подготовка/составление запроса к API
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

# Запрос к API и получение JSON
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

# Парсинг JSON
    try:
        js = json.loads(data)
    except:
        js = None

# Извлечение place_id и вывод результата
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    place_id = js['results'][0]['place_id']
    print(place_id)
