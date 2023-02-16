#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import reader
import mysql.connector
#from database.gerenciador_conexao_bd import connect
from database.gerenciador_conexao_bd import Connection
from importersiconv.gerenciador_consultas import getIDProponente 
from importersiconv.gerenciador_consultas import propostaSDI 
from datetime import date, datetime
from util.stringUtil import removeNonASCIICharacters

def salvarPropostas(arquivo_csv_propostas):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_propostas = 0
    with open(arquivo_csv_propostas, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            COD_ORGAO = linha[12].strip()
            #Só devo considerar as propostas do SDI/MAPA
            ID_PROPOSTA = linha[0].strip()
            if not propostaSDI(ID_PROPOSTA):
                continue
            UF_PROPONENTE = linha[1].strip()
            MUNIC_PROPONENTE = linha[2].strip().replace("'", "\\'")
            COD_MUNIC_IBGE = linha[3].strip()
            COD_ORGAO_SUP = linha[4].strip()
            DESC_ORGAO_SUPERIOR = linha[5].strip()
            NATUREZA_JURIDICA = linha[6].strip()
            NR_PROPOSTA = linha[7].strip()

            DIA_PROPOSTA = linha[11].strip()
            if DIA_PROPOSTA != '':
                dia_p = datetime.strptime(DIA_PROPOSTA, '%d/%m/%Y').date()
                DIA_PROPOSTA = dia_p.strftime('%Y-%m-%d')

            DESC_ORGAO = linha[13].strip()
            MODALIDADE = linha[14].strip()
            IDENTIF_PROPONENTE = linha[15].strip()
            NM_PROPONENTE = linha[16].strip().replace("'", "\\'")
            CEP_PROPONENTE = linha[17].strip()
            ENDERECO_PROPONENTE = linha[18].strip().replace("'", "\\'")
            BAIRRO_PROPONENTE = linha[19].strip().replace("'", "\\'")
            NM_BANCO = linha[20].strip()
            SITUACAO_CONTA = linha[21].strip()
            SITUACAO_PROJETO_BASICO = linha[22].strip()
            SIT_PROPOSTA = linha[23].strip()

            DIA_INICIO_VIGENCIA_PROPOSTA = linha[24].strip()
            if DIA_INICIO_VIGENCIA_PROPOSTA != '':
                dia_i = datetime.strptime(DIA_INICIO_VIGENCIA_PROPOSTA, '%d/%m/%Y').date()
                DIA_INICIO_VIGENCIA_PROPOSTA = dia_i.strftime('%Y-%m-%d')

            DIA_FIM_VIGENCIA_PROPOSTA = linha[25].strip()
            if DIA_FIM_VIGENCIA_PROPOSTA != '':
                dia_f = datetime.strptime(DIA_FIM_VIGENCIA_PROPOSTA, '%d/%m/%Y').date()
                DIA_FIM_VIGENCIA_PROPOSTA = dia_f.strftime('%Y-%m-%d')

            OBJETO_PROPOSTA = removeNonASCIICharacters(linha[26].strip()).replace("'", "\\'")
            ITEM_INVESTIMENTO = linha[27].strip().replace("'", "\\'")
            ENVIADA_MANDATARIA = linha[28].strip()
            NOME_SUBTIPO_PROPOSTA = linha[29].strip().replace("'", "\\'")
            DESCRICAO_SUBTIPO_PROPOSTA = linha[30].strip().replace("'", "\\'")
            VL_GLOBAL_PROPOSTA = linha[31].strip().replace(",", ".")
            VL_REPASSE_PROPOSTA = linha[32].strip().replace(",", ".")
            VL_CONTRAPARTIDA_PROPOSTA = linha[33].strip().replace(",", ".")

            ID_PROPONENTE = getIDProponente(IDENTIF_PROPONENTE)
            if ID_PROPONENTE == 0:
                ID_PROPONENTE = "NULL"

            #sql = "INSERT INTO Proposta (ID_PROPONENTE, Modalidade_Proposta, Situacao_Conta, \
            #    Situacao_Projeto_Basico, Situacao_Proposta, Codigo_Proposta, UF_Proponente, Municipio_Proponente, \
            #    Cod_Municipio_IBGE, Cod_Orgao_Superior, Desc_Orgao_Superior, Natureza_Juridica, Nr_Proposta, \
            #    Data_Proposta, Cod_Orgao, Desc_Orgao, Nome_Proponente, CEP_Proponente, Endereco_Proponente, Bairro_Proponente, \
            #    Nome_Banco, Data_Inicio_Vigencia, Data_Fim_Vigencia, Objeto_Proposta, Item_Investimento, Enviada_Mandataria, \
            #    Valor_Global_Proposta, Valor_Repasse_Proposta, Valor_Contrapartida_Proposta) VALUES(%d, %s, %s, %s, %s, %d, %s, %s \
            #    %d, %d, %s, %s, %s, %s, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d)"
            
            #Está dando problema inserir com tupla. Verificar depois o motivo
            #values = (ID_PROPONENTE, MODALIDADE, SITUACAO_CONTA, SITUACAO_PROJETO_BASICO, SIT_PROPOSTA, ID_PROPOSTA, \
            #       UF_PROPONENTE, MUNIC_PROPONENTE, COD_MUNIC_IBGE, COD_ORGAO_SUP, DESC_ORGAO_SUPERIOR, NATUREZA_JURIDICA, \
            #        NR_PROPOSTA, DIA_PROPOSTA, COD_ORGAO, DESC_ORGAO, NM_PROPONENTE, CEP_PROPONENTE, ENDERECO_PROPONENTE, \
            #        BAIRRO_PROPONENTE, NM_BANCO, DIA_INICIO_VIGENCIA_PROPOSTA, DIA_FIM_VIGENCIA_PROPOSTA, OBJETO_PROPOSTA, \
            #        ITEM_INVESTIMENTO, ENVIADA_MANDATARIA, VL_GLOBAL_PROPOSTA, VL_REPASSE_PROPOSTA, VL_CONTRAPARTIDA_PROPOSTA)

            sql = "INSERT INTO Proposta (ID_PROPONENTE, Modalidade_Proposta, Situacao_Conta, \
                    Situacao_Projeto_Basico, Situacao_Proposta, Codigo_Proposta, UF_Proponente, Municipio_Proponente, \
                    Cod_Municipio_IBGE, Cod_Orgao_Superior, Desc_Orgao_Superior, Natureza_Juridica, Nr_Proposta, \
                    Data_Proposta, Cod_Orgao, Desc_Orgao, Nome_Proponente, CEP_Proponente, Endereco_Proponente, Bairro_Proponente, \
                    Nome_Banco, Data_Inicio_Vigencia, Data_Fim_Vigencia, Objeto_Proposta, Item_Investimento, Enviada_Mandataria, \
                    Valor_Global_Proposta, Valor_Repasse_Proposta, Valor_Contrapartida_Proposta) VALUES (" + str(ID_PROPONENTE) + \
                    ", '" + str(MODALIDADE) + "','" + str(SITUACAO_CONTA) + "','" + str(SITUACAO_PROJETO_BASICO) + "','" + \
                    str(SIT_PROPOSTA) + "'," + str(ID_PROPOSTA) + ",'" + str(UF_PROPONENTE) + "','" + str(MUNIC_PROPONENTE) + \
                    "'," + str(COD_MUNIC_IBGE) + "," + str(COD_ORGAO_SUP) + ",'" + str(DESC_ORGAO_SUPERIOR) + "','" + \
                    str(NATUREZA_JURIDICA) + "','" + str(NR_PROPOSTA) + "','" + str(DIA_PROPOSTA) + "'," + str(COD_ORGAO) + \
                    ",'" + str(DESC_ORGAO) + "','" + str(NM_PROPONENTE) + "','" + str(CEP_PROPONENTE) + "','" + str(ENDERECO_PROPONENTE) + \
                    "','" + str(BAIRRO_PROPONENTE) + "','" + str(NM_BANCO) + "','" + str(DIA_INICIO_VIGENCIA_PROPOSTA) + "','" + \
                    str(DIA_FIM_VIGENCIA_PROPOSTA) + "','" + str(OBJETO_PROPOSTA) + "','" + str(ITEM_INVESTIMENTO) + "','" + \
                    str(ENVIADA_MANDATARIA) + "'," + str(VL_GLOBAL_PROPOSTA) + "," + str(VL_REPASSE_PROPOSTA) + "," + \
                    str(VL_CONTRAPARTIDA_PROPOSTA) + ")"

            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_propostas = numero_propostas + 1
            except:
                print("Erro ao gravar Proposta %s" % ID_PROPOSTA)
                continue
    
    print("Gravados %d Propostas" % (numero_propostas))