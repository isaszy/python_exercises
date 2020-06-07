#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:34:35 2020

@author: isinha
"""


def posso_fazer (idade: int) -> str:
    pode = ''
    if idade >= 16:
        pode += 'Você pode votar! '
    else:
        pode += 'Não pode fazer muita coisa :('
    if idade >= 18:
        pode += 'Você pode dirigir!'
    return pode
        
teste = int(input())
print(posso_fazer(teste))
