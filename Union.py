# -*- coding: utf-8 -*-

list1 = [1,3,2,4,5,6]
list2 = [1,2,4,8,9,8,7]

# Union method 1 - with duplicates
print (list1 + list2)


# Union method 2
print list(set(list1).union(set(list2)))


# Union method 3
print list(set(list1) | set(list2))


# Intersection method 1
print list(set(list1).intersection(set(list2)))


# Intersection method 2
print list(set(list1) & set(list2))


#Intersection method 3
list3 = [i for i in list1 if i in list2]
print (list3)

