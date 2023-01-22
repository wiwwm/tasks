# https://tproger.ru/translations/regular-expression-python/
"""
регулярные выражения, регулярки - шаблоны, которые используются для поиска соответсвующего фрагмента
текста и сопоставления символов, короче штука дополняющая срезы(как по мне), зная срезы и регулярки
можно делать все, что угодно
"""

# решенная задача с применением модуля re
# оригинал ../stepik2/main.py

import re
import math

i = 0
num = 0
sum_nums = 0
arr = []
s = ''
file = open('txt_files/ping.txt', 'r')
for line in file:
    result = re.findall(r'\d+мс', line)
    print(result)
    try:
        s = result[0]
    except:
        pass
    if s != '':
        num = int(s.replace('мс', ''))
        i += 1
        sum_nums += num
        arr.append(num)
file.close()
print(min(arr), math.ceil(sum_nums / i), max(arr))