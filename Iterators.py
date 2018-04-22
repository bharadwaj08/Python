# -*- coding: utf-8 -*-
"""
Demonstrate]ing efficient way of using of iterators and loops 

"""
cars = ["Aston", "Audi", "McLaren"]

#Using normal loop
for i in cars:
    print (i)

#Using index
for i in range(len(cars)):
    print (cars[i])

#Using enumerate method 1
for i,x in enumerate(cars):
    print (x)

#Using enumerate method 1
for i in enumerate(cars):
    print (i[1])    