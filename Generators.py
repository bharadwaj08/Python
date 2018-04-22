# -*- coding: utf-8 -*-

def func1():
  a = 0
  while True:
      a+=1
      return a
 
def func2():
	a = 0
	while True:
		a += 1
		yield a
 
f1 = func1()
f2 = func2()

for i in range(5):
  returnval = f1
  yieldval = next(f2)

print (returnval)
print (yieldval)
"""
def func():
	for i in range(5):
		return i

for f in func():
    print (f)
""" 



