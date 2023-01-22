"""
Совершенное число - натуральное число,
равное сумме всех своих собственных делителей.
Например, число 6 равно сумме своих собственных делителей 1 + 2 + 3.
Вам необходимо написать программу, которая выводит все совершенные числа меньшие n.

На вход программа получает число n

На выходе программа должна вывести совершенные числа меньшие n через пробел.
"""

# the best time handling is 19 sec
import time
N = int(input())
start = time.time()
for_solve = 0
tmp_arr = []
tmp = 0
""" handling perfect numbers """
for num in range(1, N):
    for des in range(1, num + 1):
        if tmp == num:
            if des == num:
                tmp_arr.append(tmp)
                break
        for_solve = num / des
        if type(for_solve) is float:
            if for_solve != int(for_solve):
                pass
            else:
                tmp += des
    tmp = 0
end = time.time() - start
for i in tmp_arr:
    print(i, end=" ")
print(end)