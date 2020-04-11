#!/usr/bin/env python
# coding: utf-8


# Меньшее из двух четных чисел: напишите функцию, которая возвращает меньшее из двух чисел, если оба эти числа четные
# иначе возвращает большее из двух чисел если одно или оба числа нечетные;

def myfuvc(num1, num2):
    if (num1%2 == 0) and (num2%2 == 0):
        return min(num1, num2)
    else: 
        return max(num1, num2)

myfuvc(2, 3)


# Напишите функцию, которая получает на входе строку из двух слов, и возвращает True, если оба слова начинаются 
# с одной и той же буквы

def myfunc1(text):
    mylist = text.lower().split()
    return mylist[0][0] == mylist[1][0]

myfunc1('Kol Lam')

# На входе два числа, функция возвращает True если сумма этих чисел равна 20, или если одно из чисел равно 28. В
# противном случае False

def myfunc2(num1, num2):
    return (num1+num2)==20 or num1 == 28 or num2 == 28

myfunc2(28, 10)


# Напишите функцию, оторая переводит  верхний регистр первую и четвертую буквы имени
def name(word):
    return word[0].upper()+word[1:3]+word[3].upper()+word[4:]

name('macdonald')

# ИЛИ

def name(word):
    first_half = word[:3]
    second_half = word[3:]
    return first_half.capitalize() + second_half.capitalize()

name('macdonald')


# На входе фраза, на выходе вернуть слова в обратном порядке
def phrase(words):  
    mylist = words.split()
    return ' '.join(mylist[::-1])

phrase('We are ready')

# На входе число n, вернуть True если n находится не далее чем на 10 от чисел 100 или 200

def n_num(n):  
    return abs(100 - n)<=10 or abs(200 - n)<=10

n_num(189)

# На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3

def three(nums):
    for i in range(0, len(nums)):
        if nums[i:i+2]==[3,3]:
            return True
    return False

three([1, 2, 3 , 3, 1])

# На входе строка, вернуть строку, где каждый символ исходной строки повтряется 3 раза

def repeat(text):
    repeat_string = ''
    
    for char in text:
        repeat_string += char*3
    return repeat_string

repeat('Hello')

# На входе три числа от 1 до 11. Если их сумма меньше или равна 21, то вернуть их сумму. Если сумма больше 21 и среди чисел
# есть 11, то уменьшить общую сумму на 10. Если сумма (и после уменьшения) больше 21, вернуть 'BUST'

def sums(a, b, c):
    summa = a + b + c
    if sum([a, b, c])<= 21:
        return sum([a, b, c])
    elif sum([a, b, c])>= 21 and (a or b or c)==11:
        return sum([a, b, c])-10
    else:
         return 'Bust'

sums(11, 11, 9)

# Вернуть сумму чисел в массиве, кроме набора чисел который начинается с 6 и продолжается до 9. Вернуть 0, если чисел нет

def sums(arr):
    result = 0
    add = True
    
    for num in arr:
        while add:
            if num != 6:
                result +=num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return result

sums([2, 1, 6, 9, 11])

# Напишите функцию, которая берет список чисел, и возвращает True, если в списке содержатся числа 0 0 7 в указанном порядке

def sums(arr):
    code = [0, 0, 7, 'x']
    for num in arr:
        if num == code[0]:
            code.pop(0)
    return len(code)==1

sums([0, 0, 6, 9, 7])

# Напишите функцию, которая возвращает количество простых чисел, который меньше или равны указанному числу

def simple_nums(num):
    if num<2:
        return 0 
    # 0 и 1 не являются простыми числами
    primes= [2]
    x=3
    while x<=num:
        for y in primes:
            if x%y == 0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
            
    print(primes)
    return len(primes)

simple_nums(100)


# Напишите функцию, которая принимает на вход одну букву, и возвращает фигуру 5Х5 для этой буквы для ABCDE 

def print_big(letter):
    shablons = {1: '  *  ', 2:' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8:'*  * ', 9: '*    ' }
    alpha = {'A':[1, 2, 4, 3, 3], 'B':[5,3,5,3,5], 'C':[4,9,9,9,4], 'D':[5,3,3,3,5], 'E':[4,9,4,9,4]}
    for shablon in alpha[letter.upper()]:
        print(shablons[shablon])

print_big('a')

# "Тайный язык" 
# берется слово на английском
# если первая буква гласная, то добавляем в конце слова 'ay'
# если первая буква согласная, то переносим первую букву в конец слова, и добавляем  концу 'ay'

def lang(word):
        if word[0] in ['aeiuyo']:
            new_word = word + 'ay'
        else:
            new_word = word[1:]+word[0]+'ay'
        return new_word       

lang('word')





