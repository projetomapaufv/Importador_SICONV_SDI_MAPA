#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode 

class Connection:
	connection = None
	cursor = None
	bufferedCursor = None

	def connect():
		try:
			if Connection.connection is None:
				print("Criou nova conexão")
				Connection.connection = mysql.connector.connect(host='localhost', user='root', password='v1s2r3@@', database='Convenios_Mapa')
			
			return Connection.connection
		except mysql.connector.Error as error:
			if error.errno == errorcode.ER_BAD_DB_ERROR:
				print("Banco de dados não existe!")
			elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Usuário ou senha incorretos!")
			else:
				print(error)
		else:
			Connection.connection.close()

	def getConnection():
		return Connection.connection
	
	def getCursor():
		if Connection.cursor is None:
			Connection.cursor = Connection.connection.cursor()
		return Connection.cursor

	def getBufferedCursor():
		if Connection.bufferedCursor is None:
			Connection.bufferedCursor = Connection.connection.cursor(buffered=True)
		return Connection.bufferedCursor