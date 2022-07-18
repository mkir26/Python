# Проверка введенного с клавиатуры числа на простое число Вильсона
# Простое число Вильсона - это простое целое число p, такое, что p*p делит (p-1)! + 1
import re
print('Let\'s check you number for Wilson Prime!')
x = input('Please, input one positive integer prime number: ')
# Проверка пользовательского ввода
if re.search('^[0-9]+', x) is None:
    print('Please, choose only only positive digits!')
    quit()
try: int(x)
except:
    print('Please, input only integer number!')
    quit()
# Почему формула не работает с 0 или 1 надо спросить у математиков)
if int(x) == 0 or int(x) == 1:
    print('Please, not zero OR one! Try again.')
    quit()
# Проверка введенного числа на простоту (не мой алгоритм)
p = int(x)
for n in range(2,int(p**0.5)+1):
    if p%n==0:
        print('Please, inter a prime number!')
        quit()
# Начало вычислений по формуле ((P-1)! + 1) / (P * P)
count = 1
# Вычисление факториала (P-1)!
for i in range(1, p): count *= i
# Финальное вычисление по формуле и вывод результата вычислений.
# Если остаток от деления целое число, то мы нашли простое число Вильсона!
if (count + 1)%(p ** 2) == 0: print('Congratulations! You number:', p, 'is a Wilson Prime!')
else: print('Oh, no. You number:', p, 'is not a Wilsons Prime. Try harder!')

# Код написанный для CodeWars. Числа более 1000 не проверяются, нет смысла.
#def am_i_wilson(n):
#    import math
#    if n <= 1 or n > 1000: return False
#    for pr in range(2,int(n**0.5)+1):
#        if pr%n==0: return False
#    if (math.factorial(n - 1) + 1) % (n ** 2) == 0: return True
#    return False
