# Программа на базе: http://www.py4e.com/code3/emaildb.py
# Парсинг текстового файла: http://www.py4e.com/code3/mbox.txt
# Запись результатов в SQL базу данных (SQLite)
import sqlite3

# Cоздаем/пересоздаем базу emaildb и таблицу Counts в случае ее наличия
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

# Парсинг текстового файла с подсчетом кол-ва email соответствущих домену
counts = {}
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org_ = pieces[1].split('@')
    counts[org_[1]] = counts.get(org_[1], 0) + 1

# Запись результатов парсинга в базу данных
for k, v in counts.items():
    cur.execute('''INSERT INTO Counts (org, count)
                   VALUES (?, ?)''', (k, v))
conn.commit()

# Вывод результатов
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr): print(str(row[0]), row[1])
cur.close()
