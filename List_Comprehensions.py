# -*- coding: utf-8 -*-

# Different ways of using lists

x = [x * x for x in range(10)]
print(x)


x = [x for x in input("Enter string: ").upper()]
print ("".join(x))


d = {x: x*x for x in range(10)}
print (d)

###################################

lis = [1,2,8,8,2,4,5]
print (set(lis))

##########################
s = 0
for x in lis:
    s += x
print (s)

d = {x.upper(): x*3 for x in 'acbd'}
print(d)













    






