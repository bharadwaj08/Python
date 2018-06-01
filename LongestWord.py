# -*- coding: utf-8 -*-

# Find the longest word from a list of words

def longest(wordlis):
    wordlen = []
    for n in wordlis:
        wordlen.append((len(n), n))
    wordlen.sort()
    return wordlen[-1][1]

print(longest(["Hi", "Hello"]))





    

