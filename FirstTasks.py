#!/usr/bin/env python
# coding: utf-8

# Написать команду, которая выведет только те слова, которые начинаются с буквы 's'
st = 'Print only the words that starts with s in this sentence'

for words in st.split():
    if words[0].lower() == 's':
        print(words)







