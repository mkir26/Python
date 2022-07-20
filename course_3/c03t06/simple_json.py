# Скрипт на основе кода https://www.py4e.com/code3/json2.py
# Загрузка JSON документа с внешнего ресурса. Парсинг JSON. Операции со значениями.
# Тестовый JSON: http://py4e-data.dr-chuck.net/comments_42.json
# Контрольный JSON: http://py4e-data.dr-chuck.net/comments_1593848.json

import urllib.request, urllib.parse, urllib.error
import json

# Пользовательский ввод и загрузка JSON документа
url = input('Please, input URL (JSON doc):')
if url == '' : quit()
json_ = urllib.request.urlopen(url).read().decode()
print('Retrieving', url)
print('Retrieved', len(json_), 'characters')

# Подключение парсера JSON
info_ = json.loads(json_)

# Проходка по тегам ключам 'count' с подсчетом кол-ва значений и их суммы
count = 0
sum_ = 0
for item in info_['comments']:
    count += 1
    sum_ = sum_ + int(item['count'])

# Результат подсчета количества значений и их сумма
print('Count:', count)
print('Sum:', sum_)
