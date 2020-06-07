#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:15:06 2020

@author: isinha
"""
def FizzBuzz (x: int) -> str:
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return x
    
    
def FizzBuzzRetorno (n: int) -> str:
    for i in range(1, n+1):
        print (FizzBuzz(i))

teste = int(input())
print(FizzBuzzRetorno(teste))
    