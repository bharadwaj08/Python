# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:38:57 2018

@author: bbsbh
"""
#method 1 to find second highest 
arr = [2,3,5,5,6,5,4,6,6]
a = sorted(list(set(arr)))
print (a[-2])


#method 2 
b = max(arr)
while max(arr) == b:
    arr.remove(b)
print (max(arr))