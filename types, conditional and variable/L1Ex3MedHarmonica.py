#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:36:24 2020

@author: isinha
"""
def media (x: float, y: float) -> float:
    media = (x + y)/2
    return media

def reciproco(x: float) -> float:
    reciproco = 1/x
    return reciproco


def media_harmonica(x: float, y: float) -> float:
    harmonicaV1 = 2 / (1/x + 1/y)
    harmonicaV2 = media(reciproco(x), reciproco(y))**-1
    return (harmonicaV1, harmonicaV2)
    
