#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:08:26 2020

@author: isinha
"""


def triangulo (a: float, b: float, c: float) -> str:
    if a + b > c or b + c > a or a + c > b:
        return 'É lado de triângulo'
    else:
        return 'Não é lado de triângulo'