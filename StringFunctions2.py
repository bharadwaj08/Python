# -*- coding: utf-8 -*-

a = "this is a test"

# First two and last two characters of the string
print (a[0:2] + a[-2:])

# No of occurences of each character in the string
dic = {}
for n in a:
    keys = dic.keys()
    if n in keys:
       dic[n] += 1
    else:
       dic[n] = 1
print (dic)

# Remove nth index character
s = input("Enter string: ")
i = input("Enter index: ")
first = s[:i]
last = s[i+1:]
print(first + last)


