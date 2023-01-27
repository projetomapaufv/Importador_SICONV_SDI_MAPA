#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata

def removeNonASCIICharacters(value):
    return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')

#Verifica se o campo é vazio. Caso for vazio, retorna NULL
def checarCampoVazio(campo):
    if campo == '':
        return "NULL"
    return campo