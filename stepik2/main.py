"""
В файле дан результат работы команды ping,
Вам необходимо подсчитать среднее,
минимальное и максимальное время ответа сервера.
Все числа необходимо округлить до целого и записать через пробел в следующем порядке:
минимальное, среднее, максимальное.
Ответ должен выглядеть следующим образом:
1 100 250
"""

"""
Задача решена через срезы
"""

import math
arr_for_nums = []
count_nums = 0
sum_nums = 0
""" open file ping.txt and reading lines """
file = open('ping.txt', 'r')
for line in file:
    """ making a slice and add create temp array """
    temp_arr = line[45:].split(' ')
    """ exception hadling for lines nonconvert into int then sum all nums and count nums for calculating average num """
    try:
        arr_for_nums.append(int(temp_arr[0][:len(temp_arr[0])-2]))
        sum_nums += int(temp_arr[0][:len(temp_arr[0])-2])
        count_nums += 1
    except:
        pass
file.close()
""" calculatin average num and with decision """
average_num = sum_nums / count_nums
print(min(arr_for_nums), math.ceil(average_num), max(arr_for_nums), end=" ")


"""
В файле дан результат работы команды ping,
Вам необходимо подсчитать среднее,
минимальное и максимальное время ответа сервера.
Все числа необходимо округлить до целого и записать через пробел в следующем порядке:
минимальное, среднее, максимальное.
Ответ должен выглядеть следующим образом:
1 100 250
"""

"""
задача решена через модуль re
"""

# ../roadmaplearning/regex.py