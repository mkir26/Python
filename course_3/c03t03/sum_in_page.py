# Подсчитываем сумму всех чисел на веб - странице
# Используется внешняя библиотека BeautifulSoup ./bs4
import urllib.request, urllib.error, urllib.response, urllib.parse
from bs4 import BeautifulSoup
# Запрашиваем пользователя URL адрес веб - страницы
print('Please, make you choise [1-3]: ')
print('1 - http://py4e-data.dr-chuck.net/comments_42.html')
print('2 - http://py4e-data.dr-chuck.net/comments_1593845.html')
print('3 - other url [IN PROGRESS]')
ch = input(':')
# Фильтруем пользовательский ввод. Ручной ввод URL не реализован.
try:
    int(ch)
except:
    print('Please, enter 1, 2 or 3. Try again.')
    quit()
if int(ch) > 3 or int(ch) <= 0:
    print('Please, enter 1, 2 or 3. Try again.')
    quit()
if int(ch) == 1: url = 'http://py4e-data.dr-chuck.net/comments_42.html'
else: url = 'http://py4e-data.dr-chuck.net/comments_1593845.html'
# Получаем и парсим веб - страницу
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

print(soup)
