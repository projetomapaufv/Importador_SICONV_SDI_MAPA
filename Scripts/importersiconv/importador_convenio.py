#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import connect
from datetime import date, datetime

UG_SDI_MAPA = '420013'

def salvarConvenios(arquivo_csv_convenios):
    db_connection = connect()

    numero_linhas_csv = 0
    numero_convenios = 0
    with open(arquivo_csv_convenios, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            UG_EMITENTE = linha[12].strip()
            if UG_EMITENTE != UG_SDI_MAPA:
                continue
            NR_CONVENIO = linha[0].strip()
            ID_PROPOSTA = linha[1].strip()
            DIA_ASSIN_CONV = linha[5].strip()
            if DIA_PROPOSTA != '':
                dia_p = datetime.strptime(DIA_PROPOSTA, '%d/%m/%Y').date()
                DIA_PROPOSTA = dia_p.strftime('%Y-%m-%d')
            SIT_CONVENIO = linha[6].strip()
            SUBSITUACAO_CONVENIO = linha[7].strip()
            SITUACAO_PUBLICACAO = linha[8].strip()
            INSTRUMENTO_ATIVO = linha[9].strip()
            IND_OPERA_OBTV = linha[10].strip()
            NR_PROCESSO = linha[11].strip()
            DIA_PUBL_CON = linha[13].strip()
            DIA_INICIO_VIGENCIA = linha[14].strip()
            DIA_FIM_VIGENC_CONV = linha[15].strip()
            DIA_FIM_VIGENC_ORIGINAL_CONV = linha[16].strip()
            DIAS_PREST_CONTAS = linha[17].strip()
            DIA_LIMITE_PREST_CONTAS = linha[18].strip()
            DATA_SUSPENSIVA = linha[19].strip()
            DATA_RETIRADA_SUSPENSIVA = linha[20].strip()
            DIAS_CLAUSULA_SUSPENSIVA = linha[21].strip()
            SITUACAO_CONTRATACAO = linha[22].strip()
            IND_ASSINADO = linha[23].strip()
            MOTIVO_SUSPENSAO = linha[24].strip()
            IND_FOTO = linha[25].strip()
            QTDE_CONVENIOS = linha[26].strip()
            QTD_TA = linha[27].strip()
            QTD_PRORROGA = linha[28].strip()
            VL_GLOBAL_CONV = linha[29].strip()
            VL_REPASSE_CONV = linha[30].strip()
            VL_CONTRAPARTIDA_CONV = linha[31].strip()
            VL_EMPENHADO_CONV = linha[32].strip()
            VL_DESEMBOLSADO_CONV = linha[33].strip()
            VL_SALDO_REMAN_TESOURO = linha[34].strip()
            VL_SALDO_REMAN_CONVENENTE = linha[35].strip()
            VL_RENDIMENTO_APLICACAO = linha[36].strip()
            VL_INGRESSO_CONTRAPARTIDA = linha[37].strip()
            VL_SALDO_CONTA = linha[38].strip()
            VALOR_GLOBAL_ORIGINAL_CONV = linha[39].strip()