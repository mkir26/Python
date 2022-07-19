# Программа (паук) рекурсивной проходки по URL адресам с веб-страницы
# Для парсинга HTML используется внешняя библиотека BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Обход проблем с SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Функция загрузки HTML документа с веб-адреса. Возвращает облако тегов
def html_doc(URL, TAG):
    html = urllib.request.urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup(TAG)
    return tags

# Пользовательский ввод и начальный счетчик для цикла
url = input('Enter URL- ')
count = input('Enter count: ')
pos = input('Enter position: ')
int_count = int(count)
int_pos = int(pos)
i = 0

# Ищем int_pos строку с URL, переходим по ней и снова ищем int_pos строку URL и так int_count раз
while i <= int_count:
    print('Retrieving:', url)
    tag_cloud = html_doc(url,'a')
    tag = tag_cloud[int_pos - 1]
    url = tag.get('href', None)
    i += 1
