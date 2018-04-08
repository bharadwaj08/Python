# -*- coding: utf-8 -*-
"""
Fibonacci series in three different ways
"""
#Normal approach

n = int(input("Enter a number: "))
a = 0
b = 1   
for i in range(n):        
    a,b = b,a+b  
    print (a)
        
#Using Recursion
n = int(input("Enter a number: "))

def fib(n):
 if n==0:
     return 0
 elif n==1:
     return 1
 else:
     return fib(n-1)+fib(n-2)

print (fib(n))

#Using a range of numbers

startnum = int(input("Enter a start number: "))
endnum = int(input("Enter an end number: "))
def fib(n):
 if n==0:
     return 0
 elif n==1:
     return 1
 else:
     return fib(n-1)+fib(n-2)

for i in range(startnum, endnum):
    print (fib(i))
    
