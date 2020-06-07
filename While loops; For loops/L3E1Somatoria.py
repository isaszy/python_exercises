#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:02:51 2020

@author: isinha
"""

def somatoria (n: int) -> int:
    soma = 0
    if n < 0:
        return 0
    for i in range (1, n+1):
        soma += i
    return soma

teste = int(input())
print(somatoria(teste))