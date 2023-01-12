#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode 

#carregar dados de conexão de um arquivo de configuração
server = 'localhost'
user = 'root'
password = 'v1s2r3@@'
db = 'Convenios_Mapa'

def connect():
	try:
		db_connection = mysql.connector.connect(host='localhost', user='root', password='v1s2r3@@', database='Convenios_Mapa')
		
		return db_connection
	except mysql.connector.Error as error:
		if error.errno == errorcode.ER_BAD_DB_ERROR:
			print("Banco de dados não existe!")
		elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Usuário ou senha incorretos!")
		else:
			print(error)
	else:
		db_connection.close()