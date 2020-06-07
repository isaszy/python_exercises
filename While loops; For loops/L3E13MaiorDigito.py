#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:29:35 2020

@author: isinha
"""


def ultimoDigito (n: int) -> int:
    return n % 10

def removeDigito (n: int) -> int:
    return n // 10

def maior_digito(n: int) -> int:
    maior = ultimoDigito(n)
    novo = 0
    while n > 0:
        if novo > maior:
            maior = novo
        n = removeDigito(n)
        novo = ultimoDigito(n)
    return maior

n = int(input())
print(maior_digito(n))