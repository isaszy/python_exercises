#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:24:01 2020

@author: isinha
"""


def ultimoDigito (n: int) -> int:
    return n % 10

def removeDigito (n: int) -> int:
    return n // 10

def produtoria_digitos(n: int) -> int:
    prod = 1
    while n > 0:
        prod *= ultimoDigito(n)
        n = removeDigito(n)
    return prod

n = int(input())
print(produtoria_digitos(n))