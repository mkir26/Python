# Скрипт на основе кода https://www.py4e.com/code3/geoxml.py
# Загрузка XML документа с внешнего ресурса. Парсинг XML. Операции со значениями.
# Тестовый XML: http://py4e-data.dr-chuck.net/comments_42.xml
# Контрольный XML: http://py4e-data.dr-chuck.net/comments_1593847.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Пользовательский ввод и загрузка XML документа
url = input('Please, input URL (XML doc):')
xml = urllib.request.urlopen(url).read().decode()
print('Retrieving', url)
print('Retrieved', len(xml), 'characters')

# Подключение парсера XML
pars = ET.fromstring(xml)
lst = pars.findall('.//comment')

# Проходка по тегам <count> с подсчетом кол-ва значений и их суммы
count = 0
sum_ = 0
for i in lst:
    count += 1
    sum_ = sum_ + int(i.find('count').text)
print('Count:', count)
print('Sum:', sum_)
