#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:20:31 2020

@author: isinha
"""

def mdc (a: int, b: int) -> int:
    auxb = 0
    while a != 0 and b != 0:
        auxb = b
        b = a % b
        a = auxb
    if a == 0:
        return b
    else:
        return a
        

print(mdc(3, 6))