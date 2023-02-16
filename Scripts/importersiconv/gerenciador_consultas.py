#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import reader
import mysql.connector
#from database.gerenciador_conexao_bd import connect
from database.gerenciador_conexao_bd import Connection

def getIDProponente(CNPJ_Proponente):
    #connection = Connection()
    db_connection = Connection.connect()

    sql = "SELECT ID_Proponente FROM Proponente WHERE CNPJ = {cnpj}".format(cnpj = CNPJ_Proponente)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    proponente_encontrado = False
    for (ID_Proponente) in cursor:
        id_proponente = ID_Proponente
        proponente_encontrado = True

    #cursor.close()
    db_connection.commit()

    if proponente_encontrado:
        return id_proponente[0]
    else:
        return 0
    
def propostaSDI(codigo_proposta):
    #connection = Connection()
    db_connection = Connection.connect()

    sql = "SELECT Codigo_Proposta FROM Propostas_SDI_MAPA WHERE Codigo_Proposta = {cod_proposta}".format(cod_proposta = codigo_proposta)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    proposta_encontrada = False
    for (ID_Proposta) in cursor:
        id_proposta = ID_Proposta
        proposta_encontrada = True

    #cursor.close()
    db_connection.commit()

    return proposta_encontrada

def getIDProposta(codigo_proposta_siconv):
    #connection = Connection()
    db_connection = Connection.connect()

    sql = "SELECT ID_Proposta FROM Proposta WHERE Codigo_Proposta = {cod_proposta_siconv}".format(cod_proposta_siconv = codigo_proposta_siconv)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    proposta_encontrada = False
    for (ID_Proposta) in cursor:
        id_proposta = ID_Proposta
        proposta_encontrada = True
        break

    #cursor.close()
    db_connection.commit()

    if proposta_encontrada:
        return id_proposta[0]
    else:
        return 0
    
def getIDConvenio(numero_convenio):
    #connection = Connection()
    db_connection = Connection.connect()

    sql = "SELECT ID_Convenio FROM Convenio WHERE Nr_Convenio = {nr_convenio}".format(nr_convenio = numero_convenio)
    #cursor = db_connection.cursor(buffered=True)
    try:
        cursor = Connection.getBufferedCursor()
        cursor.execute(sql)

        convenio_encontrado = False
        for (ID_Convenio) in cursor:
            id_convenio = ID_Convenio
            convenio_encontrado = True
            break

        #cursor.close()
        db_connection.commit()
    except:
        print("Erro ao consultar Convênio")
        print(sql)
        return 0

    if convenio_encontrado:
        return id_convenio[0]
    else:
        return 0

def getIDMetaCronoFisica(codigo_meta_siconv):
    #connection = Connection()
    db_connection = Connection.connect()

    sql = "SELECT ID_Meta_Crono_Fisico FROM Meta_Crono_Fisico WHERE Codigo_Meta_Crono_Fisico = {cd_meta_siconv}".format(cd_meta_siconv = codigo_meta_siconv)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    meta_encontrada = False
    for (ID_Meta) in cursor:
        id_meta = ID_Meta
        meta_encontrada = True
        break

    #cursor.close()
    db_connection.commit()

    if meta_encontrada:
        return id_meta[0]
    else:
        return 0

def getIDEmpenho(codigo_empenho_siconv):
    db_connection = Connection.connect()

    sql = "SELECT ID_Empenho FROM Empenho WHERE Codigo_Empenho_Siconv = {cd_empenho_siconv}".format(cd_empenho_siconv = codigo_empenho_siconv)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    empenho_encontrado = False
    for (ID_Empenho) in cursor:
        id_empenho = ID_Empenho
        empenho_encontrado = True
        break

    #cursor.close()
    db_connection.commit()

    if empenho_encontrado:
        return id_empenho[0]
    else:
        return 0

def getIDDesembolso(codigo_desembolso_siconv):
    db_connection = Connection.connect()

    sql = "SELECT ID_Desembolso FROM Desembolso WHERE Codigo_Desembolso_Siconv = {cd_desembolso_siconv}".format(cd_desembolso_siconv = codigo_desembolso_siconv)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    desembolso_encontrado = False
    for (ID_Desembolso) in cursor:
        id_desembolso = ID_Desembolso
        desembolso_encontrado = True
        break

    #cursor.close()
    db_connection.commit()

    if desembolso_encontrado:
        return id_desembolso[0]
    else:
        return 0

def getIDPagamento(nr_movimentacao_financeira):
    db_connection = Connection.connect()

    sql = "SELECT ID_Pagamento FROM Pagamento WHERE Nr_Movimentacao_Financeira = {nr_mov_fin}".format(nr_mov_fin = nr_movimentacao_financeira)
    #cursor = db_connection.cursor(buffered=True)
    cursor = Connection.getBufferedCursor()
    cursor.execute(sql)

    pagamento_encontrado = False
    for (ID_Pagamento) in cursor:
        id_pagamento = ID_Pagamento
        pagamento_encontrado = True
        break

    #cursor.close()
    db_connection.commit()

    if pagamento_encontrado:
        return id_pagamento[0]
    else:
        return 0