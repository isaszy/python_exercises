#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:55:36 2020

@author: isinha
"""

def primo (x: int, y: int) -> str:
    if x % y == 0 and x != y:
        return 'Não é primo'
    else:
        return 'Não se sabe'
