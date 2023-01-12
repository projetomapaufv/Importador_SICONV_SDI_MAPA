#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import connect

def getIDProponente(CNPJ_Proponente):
    db_connection = connect()

    sql = "SELECT ID_Proponente FROM Proponente WHERE CNPJ = {cnpj}".format(cnpj = CNPJ_Proponente)
    cursor = db_connection.cursor()
    cursor.execute(sql)

    proponente_encontrado = False
    for (ID_Proponente) in cursor:
        id_proponente = ID_Proponente
        proponente_encontrado = True

    cursor.close()
    db_connection.commit()
    db_connection.close()

    if proponente_encontrado:
        return id_proponente[0]
    else:
        return 0
    
def propostaSDI(codigo_proposta):
    db_connection = connect()

    sql = "SELECT Codigo_Proposta FROM Propostas_SDI_MAPA WHERE Codigo_Proposta = {cod_proposta}".format(cod_proposta = codigo_proposta)
    cursor = db_connection.cursor()
    cursor.execute(sql)

    proposta_encontrada = False
    for (ID_Proposta) in cursor:
        id_proposta = ID_Proposta
        proposta_encontrada = True

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return proposta_encontrada
