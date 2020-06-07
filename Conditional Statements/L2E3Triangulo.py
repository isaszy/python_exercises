#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:16:53 2020

@author: isinha
"""


"Triângulos, teste"
def eh_triangulo(a, b, c) -> str:
    if a != 0 and b != 0 and c != 0:
        if a + b > c:
            return 'É lado de um triângulo'
        elif a + c > b:
            return 'é lado de um triangulo'
        elif b + c > a:
            return 'é lado de um triangulo'
        else:
            return 'não é lado de um triangulo'
    else:
        return 'não é lado de um triangulo'

print(eh_triangulo(0, 1, 1))
