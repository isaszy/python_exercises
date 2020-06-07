#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:01:57 2020

@author: isinha
"""

def ano_bissexto(ano: int) -> bool:
    if ano % 4 != 0 or ano % 100 == 0 or ano % 400 != 0:
        return True
    else:
        return False