#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import reader
import mysql.connector
#from database.gerenciador_conexao_bd import connect
from database.gerenciador_conexao_bd import Connection
from importersiconv.gerenciador_consultas import getIDPropostaPorNumeroConvenio
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters

EVENTOS_CAPACITACAO = 'EVENTOS / CAPACITAÇÂO'
EVENTO = 'EVENTO'

#Grava os convênios do Mapa no banco de dados
def salvarMatrizMapa(arquivo_csv_matriz_mapa):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_propostas = 0
    with open(arquivo_csv_matriz_mapa, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            NR_CONVENIO = linha[0].strip()
            ID_PROPOSTA = getIDPropostaPorNumeroConvenio(NR_CONVENIO)
            #Proposta não encontrada
            if ID_PROPOSTA == 0:
                continue;
            UNID_RESP = linha[2].strip()
            RP = checarCampoVazio(linha[4].strip())
            VINCULACAO = checarCampoVazio(linha[5].strip())
            CD = linha[6].strip()
            DESCRICAO_RP = removeNonASCIICharacters(linha[7].strip())
            AUTOR = removeNonASCIICharacters(linha[8].strip())
            NUMERO_PROPOSTA = linha[9].strip()
            NUMERO_PROCESSO = linha[10].strip()
            EMPENHADO = linha[16].strip()
            PUBLICACAO = linha[17].strip()
            CATEGORIA = linha[19].strip()
            if CATEGORIA == EVENTOS_CAPACITACAO:
                CATEGORIA = EVENTO
            SUB_ROGACAO = linha[26].strip()

            sql = "UPDATE Proposta SET Unid_Resp='%s' ,RP=%s ,Vinculacao=%s, CD='%s', Descricao_RP='%s', \
                    Autor='%s', Numero_Proposta='%s', Numero_Processo='%s', Empenhado='%s', Publicacao='%s', \
                    Categoria='%s', Sub_Rogacao='%s'" % (UNID_RESP, RP, VINCULACAO, CD, DESCRICAO_RP, AUTOR, NUMERO_PROPOSTA, \
                    NUMERO_PROCESSO, EMPENHADO, PUBLICACAO, CATEGORIA, SUB_ROGACAO)
            
            try:
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                db_connection.commit()
                numero_propostas = numero_propostas + 1
            except Exception as e:
                print("Erro ao atualizar Propostas %s" % ID_PROPOSTA)
                print(str(e))
                continue
        
    
    print("Atualizadas %d Propostas" % (numero_propostas)) 