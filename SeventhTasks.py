# Создайте генератор, который создает квадраты чисел, вплоть до некторого числа N

def get_squares(n):
    for x in range(n):
        yield x**2

for num in get_squares(10):
    print(num)


# Создайте генератор, который возвращает "n" случайных чисел между нижней и верхней границами 
# (границы являются параметрами функции)

import random
def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

# Используйте функцию iter(), чтобы превратить строку ниже в итератор

s = 'hello'
s = iter(s)
print(next(iterator))

