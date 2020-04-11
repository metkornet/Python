#!/usr/bin/env python
# coding: utf-8

# Написать команду, которая выведет только те слова, которые начинаются с буквы 's'
st = 'Print only the words that starts with s in this sentence'

for words in st.split():
    if words[0].lower() == 's':
        print(words)

#  Используйте range(), чтобы распечатать все четные числа от 0 до 10

for num in range(0,11,2):
    print(num)

#  Используйте генератор списков, чтобы создать список всех чисел от 0 до 50, которые деляться на цело на 3

[num for num in range(0, 51) if num%3 == 0]

		# ИЛИ
[num for num in range(0, 51, 3)]

#  Пройдите по словам в строке ниже, и если длина слов четная, то напечатайте "Это слово имеет четную длину"

st = 'Print every words in this sentence that has an even number of letters'
for words in st.split():
    if (len(words)%2) == 0:
        print(words + ' это слово имеет четную длину')

# Напишите программу, которая напечатает числа от 0 до 100. Но для тех чисел, которые делятся нацело на 3, 
# вместо числа выведите 'Fizz', а для тех, которые нацело делятся на 5, выведите 'Buzz', а для те, которые 
# нацело делятся на 5 и 3, выведите выведите 'FizzBuzz'.

for num in range(0, 101):
    if (num%3 == 0) and (num%5 == 0):
        print('FizzBuzz')
    elif (num%3 == 0):
        print('Fizz')
    elif (num%5 == 0):
        print('Buzz')
    else:
        print(num)
#  Используйте генераторы списков, чтобы создать список первых букв из всех слов в строке ниже:

st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split() ]







