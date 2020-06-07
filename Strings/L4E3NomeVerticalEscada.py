#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:49:06 2020

@author: isinha
"""


def nome_vert_escada (nome):
    linha = []
    for letra in nome:
        linha += letra
        string = ''.join(linha)
        print(string)
    return ''


print(nome_vert_escada('erikinhozinho'))
