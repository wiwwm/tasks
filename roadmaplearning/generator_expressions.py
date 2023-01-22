# генераторное выражение - выражение, возвращающее итератор генератора
# через built-in функцию next можно вывести итератор, начиная с начала range
my_generator = (i for i in range(10)) # объект класс generator
print(next(my_generator)) # 0
print(next(my_generator)) # 1