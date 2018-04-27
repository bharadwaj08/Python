# -*- coding: utf-8 -*-

# 

def freq(list1):
 num = len(set([i for i in list1 if list1.count(i) >= 2]))
 return num

list1 = [1,1,2,3,4,4,4,5,6,6]
print (freq(list1))

