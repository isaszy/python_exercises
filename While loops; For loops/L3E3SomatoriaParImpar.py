#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:08:49 2020

@author: isinha
"""

def soma_par (n: int) -> int:
    soma = 0
    for i in range (2, n+1, 2):
        soma += i
    return soma 

def soma_impar (n: int) -> int:
    soma = 0
    for i in range (1, n+1, 2):
        soma += i
    return soma

teste = int(input())
print(soma_par(teste) + soma_impar(teste))