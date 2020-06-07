#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:26:57 2020

@author: isinha
"""


def pedra_papel_tesoura(j1: str, j2: str) -> int:
    if j1 == 'PEDRA':
        if j2 == 'TESOURA':
            return 1
        elif j2 == 'PAPEL':
            return 2
        else: 
            return 0
    elif j1 == 'TESOURA':
        if j2 == 'PAPEL':
            return 1
        elif j2 == 'PEDRA':
            return 2
        else:
            return 0
    else:
        if j2 == 'TESOURA':
            return 2
        elif j2 == 'PEDRA':
            return 1
        else: 
            return 0
