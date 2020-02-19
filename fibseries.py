#Python program to generate fibonacci series using generators.

from __future__ import generators

def fib(length):
  a,b=0,1
  while a<length:
    yield a
    a,b=b,a+b
x=fib(10)
for i in fib(10):
  print(i)