#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:17:59 2020

@author: isinha
"""

def maior_de_3 (x: float, y: float, z: float) -> float:
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z