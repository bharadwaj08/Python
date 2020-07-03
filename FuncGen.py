# -*- coding: utf-8 -*-

def attach_data(func):
       func.data = 3
       return func
 
@attach_data
def add (x, y):
       return x + y
 
# Driver code
 
# This call is equivalent to attach_data()
# with add() as parameter
print(add(2, 3))
 
print(add.data)


min = (lambda x, y: x if x < y else y)
print (min(101*99, 102*98))
