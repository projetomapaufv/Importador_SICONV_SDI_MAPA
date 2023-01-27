#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, datetime

#Converto a data para o formato do MySQL
def converteData(data):
    if data == '':
        return "NULL"

    dataDate = datetime.strptime(data, '%d/%m/%Y').date()
    dataStr = dataDate.strftime('%Y-%m-%d')

    return "'" + dataStr + "'"