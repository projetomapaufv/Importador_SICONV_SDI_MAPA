#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from database.gerenciador_conexao_bd import connect
from importersiconv.importador_proponente import salvarProponentes 
from importersiconv.importador_proposta import salvarPropostas
from importersiconv.gravaPropostasSDI import salvarPropostasSDI

#@TODO Carregar os caminhos dos arquivos de um arquivo de configuração
ARQUIVO_PROPONENTES = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_proponentes.csv'
ARQUIVO_PROPOSTAS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_propostas.csv'
ARQUIVO_CONVENIOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_convenio.csv'

salvarProponentes(ARQUIVO_PROPONENTES)
salvarPropostasSDI(ARQUIVO_CONVENIOS)
salvarPropostas(ARQUIVO_PROPOSTAS)