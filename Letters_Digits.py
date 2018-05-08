# -*- coding: utf-8 -*-

# Program to print the number of digits and letters in a given string

s = input("Enter a string: ")
d = {"D":0, "L":0}
for ch in s:
    if ch.isdigit():
        d["D"] += 1
    elif ch.isalpha():
        d["L"] += 1
        
print ("Letters: ", d["L"])
print ("Digits: ", d["D"])

