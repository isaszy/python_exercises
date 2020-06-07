#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:17:58 2020

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
