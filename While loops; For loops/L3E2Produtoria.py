#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:06:05 2020

@author: isinha
"""

def produtoria (n: int) -> int:
    produto = 1
    if n < 0:
        return 0
    for i in range (1, n+1):
        produto *= i
    return produto

teste = int(input())
print(produtoria(teste))

#Alterar produto pra 1; e nome das variaveis e operação no for