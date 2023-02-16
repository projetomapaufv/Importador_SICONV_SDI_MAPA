#!/usr/bin/env python
# -*- coding: utf-8 -*-

from csv import reader
import mysql.connector
#from database.gerenciador_conexao_bd import connect
from database.gerenciador_conexao_bd import Connection

UG_SDI_MAPA = '420013'

def salvarPropostasSDI(arquivo_csv_convenios):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_propostas = 0
    with open(arquivo_csv_convenios, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Dados
            UG_EMITENTE = linha[12].strip()
            ID_PROPOSTA = linha[1].strip()
            if UG_EMITENTE == UG_SDI_MAPA:
                sql = "INSERT INTO Propostas_SDI_MAPA(Codigo_Proposta) VALUES(" + ID_PROPOSTA + ")"
            
                try:
                    cursor = db_connection.cursor()
                    cursor.execute(sql)
                    cursor.close()
                    db_connection.commit()
                    numero_propostas = numero_propostas + 1
                except:
                    print("Erro ao gravar Propostas_SDI_MAPA %s" % ID_PROPOSTA)
                    continue
    
    print("%d Propostas da SDI gravadas" % (numero_propostas))
