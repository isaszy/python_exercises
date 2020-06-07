#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:18:00 2020

@author: isinha
"""
import math
def eq2grau (a: float, b: float, c: float) -> tuple:
    delta = (b**2) - (4*a*c)
    if delta == 0:
        return - b / (2*a)
    elif delta > 0:
        return (- b + math.sqrt(delta)) / (2*a), (- b - math.sqrt(delta)) / (2*a)
    else:
        return None

print(eq2grau(1, 6, 3))