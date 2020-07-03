# -*- coding: utf-8 -*-


s = "bulusub"
print(s[::1])

lis = [1,1,2,3,4,3,4,4,5,3,2,7,4,8]

t = max(lis, key=lambda x: lis.count(x))

print(t)


list1 = [1,2,4,5,7,3]
list2 = [2,3,8,9,6]

res = (set(list1).difference(set(list2)))

print(res)
#------------------------------------------------

setA = {1,2,3}
setB = {'a', 'b'}
setA.update(setB)

print(setA)

#------------------------------------------------

s = 'Bharadwaj'
t = {1,2,3}

t.update(s)

print(t)