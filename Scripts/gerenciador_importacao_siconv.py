#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from database.gerenciador_conexao_bd import connect
from importersiconv.importador_proponente import salvarProponentes 
from importersiconv.importador_proposta import salvarPropostas
from importersiconv.gravaPropostasSDI import salvarPropostasSDI
from importersiconv.importador_convenio import salvarConvenios
from importersiconv.importador_empenho import salvarEmpenhos
from importersiconv.importador_licitacao import salvarLicitacoes
from importersiconv.importador_pagamento_tributo import salvarPagamentosTributos
from importersiconv.importador_prorroga_oficio import salvarProrrogaOficio
from importersiconv.importador_termo_aditivo import salvarTermosAditivos


#@TODO Carregar os caminhos dos arquivos de um arquivo de configuração
ARQUIVO_PROPONENTES = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_proponentes.csv'
ARQUIVO_PROPOSTAS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_propostas.csv'
ARQUIVO_CONVENIOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_convenio.csv'
ARQUIVO_EMPENHOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_empenho.csv'
ARQUIVO_LICITACOES = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_licitacao.csv'
ARQUIVO_PAGAMENTO_TRIBUTOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_pagamento_tributo.csv'
ARQUIVO_PRORROGA_OFICIO = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_prorroga_oficio.csv'
ARQUIVO_TERMOS_ADITIVOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_termo_aditivo.csv'

#salvarProponentes(ARQUIVO_PROPONENTES)
#salvarPropostasSDI(ARQUIVO_CONVENIOS)
#salvarPropostas(ARQUIVO_PROPOSTAS)
#salvarEmpenhos(ARQUIVO_EMPENHOS)
#salvarLicitacoes(ARQUIVO_LICITACOES)
#salvarPagamentosTributos(ARQUIVO_PAGAMENTO_TRIBUTOS)
#salvarProrrogaOficio(ARQUIVO_PRORROGA_OFICIO)
salvarTermosAditivos(ARQUIVO_TERMOS_ADITIVOS)