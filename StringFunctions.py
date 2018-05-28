# -*- coding: utf-8 -*-

# Number of occurences of each word in a string
str = input("Enter string: ")
ct = dict()
words = str.split()

for word in words:
    if word in ct:
        ct[word] += 1
    else:
        ct[word] = 1
print (ct)

