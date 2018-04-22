# -*- coding: utf-8 -*-

s = input("Enter a string: ") #use raw_input for python2

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
d1 = {letter: 0 for letter in alphabets} #initializing all alphabets, numbers to count 0

for ch in s:
 d1[ch] += 1 #incrementing count on repeat

for key in d1:
 print(key,d1[key])

