#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:07:51 2020

@author: isinha
"""


def nota_conceito(nota: float) -> str:
    if nota >= 9:
        return 'A'
    elif nota >= 8:
        return 'B'
    elif nota >= 6:
        return 'C'
    elif nota >= 5:
        return 'D'
    else:
        return 'F'