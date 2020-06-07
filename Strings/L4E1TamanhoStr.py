#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:33:42 2020

@author: isinha
"""

def tamanho_str (s1: str, s2: str) -> str:
    tamanho1 = len(s1)
    tamanho2 = len(s2)
    print(s1, tamanho1)
    print(s2, tamanho2)
    
    if tamanho1 == tamanho2:
        print('Possuem o mesmo comprimento')
        for i in range(0, tamanho1):
            if s1[i] != s2[i]:
                return 'São diferentes.'
        return 'São iguais'
                
s1 = input()
s2 = input()
print(tamanho_str(s1, s2))    
    