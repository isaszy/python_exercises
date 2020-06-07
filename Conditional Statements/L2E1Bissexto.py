#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:15:04 2020

@author: isinha
"""

'Bissexto, teste'
def bissexto (ano: int) -> str:
    if ano % 4 != 0:
        return 'não é bissexto'
    elif ano % 100 != 0:
        return 'é bissexto'
    elif ano % 400 != 0:
        return 'não é bissexto'
    else:
        return 'é bissexto'

for ano in range(2000, 2021):
    print(bissexto(ano))