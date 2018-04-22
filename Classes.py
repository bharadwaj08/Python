# -*- coding: utf-8 -*-

#Example 1
class MyClass:
    
    i = 123

    def f(self):
        return 'hello world'
    
print (MyClass.i)

#Example 2
class Complex:
   def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, 4.5)
print (x.r, x.i)