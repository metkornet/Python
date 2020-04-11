#!/usr/bin/env python
# coding: utf-8

# Напишите функцию, которая вычисляет объем сферы по заданному радиусу

def vol(rad):
    return (4/3)*(3.14)*(rad**3)
vol(2)

# Напишите функцию, которая проверяет, содержится ли число в указанном диапозоне (включая верхнюю и нижнюю границы)

def ran_check(num, low, high):
    if num in range(low, high+1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('{} is not in the range between {} and {}'.format(num, low, high))

ran_check(18, 2, 7)

# Если только True/False

def ran_check(num, low, high):
    return num in range(low, high+1)

ran_check(18, 2, 7)

# Напишите функцию, которая принимает на вход строку, и вычисляет количесвто букв в верхнем регистре и в нижнем регистре

def up_low(text):
    kolvo={'upper': 0, 'lower': 0}
    for word in text:
        if word.isupper():
            kolvo['upper']+=1
        elif word.islower():
            kolvo['lower']+=1
        else:
            pass
    print('Количество символов в верхнем регистре:', kolvo['upper'])
    print('Количество символов в нижнем регистре:', kolvo['lower'])

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Напишите функцию, которая получает на входе список, и возвращает новый список, содержащий уникальные элементы 
# из первого списка

def unique_list(lst):
    return list(set(lst))

unique_list([1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5])

# ИЛИ

def unique_list(lst):
    x = []
    for item in lst:
        if item not in x:
            x.append(item)
    return x

unique_list([1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 5])


# Напишите функцию, которая перемножает все числа в списке

def multiplay(lst):
    total=1
    for item in lst:
        total*=item
    return total

multiplay([1, 2, 3, -4])


# Напишите функцию, которая проверяет входную строку, является ли эта строка палиндромом или нет

def palindrome(word):
    word = word.replace(' ', '')
    return word==word[::-1]

palindrome('helleh')

# Напишите функцию, которая проверяет входную строку, является ли строка панграммой или нет

import string

def ispangram(str1, alpha1=string.ascii_lowercase):
    alpha2=set(alpha1)
    return alpha2<=set(str1.lower())

ispangram('The quick brown fox jumps over the lazy dog')


