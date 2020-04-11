# Обработайте исключение, которое вызывает код ниже, с помощью блоков try и except

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print('Нельзя возвести букву в квадрат')


# Обработайте исключение, которое вызывает код ниже, с помощью блоков try и except. Затем используйте блок finally,
# чтобы сказать, что все сделано

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('Деление на ноль')
finally:
    print('Все сделано')


# Напишите функцию, которая спрашивает пользователя ввести число, и затем выводит это число в квадрате.
# Используйте цикл while и блоки try, except, else для обработки некорректно введенных данных

def ask():
    while True:
        try:
            num = int(input('Введите число '))
            result = num**2
        except ValueError:
            print('Не число')
            continue
        else:
            return result
            break
        
ask()
