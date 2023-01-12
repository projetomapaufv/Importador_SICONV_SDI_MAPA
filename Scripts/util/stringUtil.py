#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata

def removeNonASCIICharacters(value):
    return unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')