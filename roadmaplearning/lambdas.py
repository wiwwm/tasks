"""
по-русски лямбды это анонимные ограниченные в функционале относительно обычных функции
которые вычисляют возвращают только одно значение
удобны для применения везде, где требуются объекты-функции
анонимные функции имеют любое количество аргументов
можно использовать с функциями высшего порядка(filter, map и др)
"""

def defined_cube(y):
    return y*y*y

# ==

lambda_cube = lambda y: y*y*y

print(defined_cube(2))
print(lambda_cube(2))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)