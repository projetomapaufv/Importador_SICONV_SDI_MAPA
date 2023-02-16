#!/usr/bin/env python
# -*- coding: utf-8 -*-
from database.gerenciador_conexao_bd import Connection
from importersiconv.importador_proponente import salvarProponentes 
from importersiconv.importador_proposta import salvarPropostas
from importersiconv.gravaPropostasSDI import salvarPropostasSDI
from importersiconv.importador_convenio import salvarConvenios
from importersiconv.importador_empenho import salvarEmpenhos
from importersiconv.importador_licitacao import salvarLicitacoes
from importersiconv.importador_pagamento_tributo import salvarPagamentosTributos
from importersiconv.importador_prorroga_oficio import salvarProrrogaOficio
from importersiconv.importador_termo_aditivo import salvarTermosAditivos
from importersiconv.importador_meta_crono_fisica import salvarMetasCronoFisicas
from importersiconv.importador_etapa_crono_fisica import salvarEtapasCronoFisicas
from importersiconv.importador_ingresso_contrapartida import salvarIngressosContrapartida
from importersiconv.importador_desembolso import salvarDesembolsos
from importersiconv.importador_empenho_desembolso import salvarEmpenhosDesembolsos
from importersiconv.importador_pagamento import salvarPagamentos
from importersiconv.importador_obtv_convenente import salvarObtvConvenente
from importersiconv.importador_desbloqueio_cr import salvarDesbloqueiosCR
from importersiconv.importador_justificativa_proposta import salvarJustificativasPropostas
from importersiconv.importador_cronograma_desembolso import salvarCronogramaDesembolso
from importersiconv.importador_historico_situacao import salvarHistoricoSituacao


#@TODO Carregar os caminhos dos arquivos de um arquivo de configuração
ARQUIVO_PROPONENTES = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_proponentes.csv'
ARQUIVO_PROPOSTAS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_propostas.csv'
ARQUIVO_CONVENIOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_convenio.csv'
ARQUIVO_EMPENHOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_empenho.csv'
ARQUIVO_LICITACOES = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_licitacao.csv'
ARQUIVO_PAGAMENTO_TRIBUTOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_pagamento_tributo.csv'
ARQUIVO_PRORROGA_OFICIO = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_prorroga_oficio.csv'
ARQUIVO_TERMOS_ADITIVOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_termo_aditivo.csv'
ARQUIVO_METAS_CRONO_FISICAS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_meta_crono_fisico.csv'
ARQUIVO_ETAPAS_CRONO_FISICAS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_etapa_crono_fisico.csv'
ARQUIVO_INGRESSOS_CONTRAPARTIDA = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_ingresso_contrapartida.csv'
ARQUIVO_DESEMBOLSO = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_desembolso.csv'
ARQUIVO_EMPENHO_DESEMBOLSO = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_empenho_desembolso.csv'
ARQUIVO_PAGAMENTOS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_pagamento.csv'
ARQUIVO_OBTV_CONVENENTE = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_obtv_convenente.csv'
ARQUIVO_DESBLOQUEIO_CR = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_desbloqueio_cr.csv'
ARQUIVO_JUSTIFICATIVAS_PROPOSTAS = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_justificativas_proposta.csv'
ARQUIVO_CRONOGRAMA_DESEMBOLSO = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_cronograma_desembolso.csv'
ARQUIVO_HISTORICO_SITUACAO = '/home/vagner/Projeto_MAPA/Arquivos_Siconv/siconv_historico_situacao.csv'

salvarProponentes(ARQUIVO_PROPONENTES)
salvarPropostasSDI(ARQUIVO_CONVENIOS)
salvarPropostas(ARQUIVO_PROPOSTAS)
salvarEmpenhos(ARQUIVO_EMPENHOS)
salvarLicitacoes(ARQUIVO_LICITACOES)
salvarPagamentosTributos(ARQUIVO_PAGAMENTO_TRIBUTOS)
salvarProrrogaOficio(ARQUIVO_PRORROGA_OFICIO)
salvarTermosAditivos(ARQUIVO_TERMOS_ADITIVOS)
salvarMetasCronoFisicas(ARQUIVO_METAS_CRONO_FISICAS)
salvarEtapasCronoFisicas(ARQUIVO_ETAPAS_CRONO_FISICAS)
salvarIngressosContrapartida(ARQUIVO_INGRESSOS_CONTRAPARTIDA)
salvarDesembolsos(ARQUIVO_DESEMBOLSO)
salvarEmpenhosDesembolsos(ARQUIVO_EMPENHO_DESEMBOLSO)
salvarPagamentos(ARQUIVO_PAGAMENTOS)
salvarObtvConvenente(ARQUIVO_OBTV_CONVENENTE)
salvarDesbloqueiosCR(ARQUIVO_DESBLOQUEIO_CR)
salvarJustificativasPropostas(ARQUIVO_JUSTIFICATIVAS_PROPOSTAS)
salvarCronogramaDesembolso(ARQUIVO_CRONOGRAMA_DESEMBOLSO)
salvarHistoricoSituacao(ARQUIVO_HISTORICO_SITUACAO)

#Fecho a conexão
db_connection = Connection.getConnection()
cursor = Connection.getCursor()
if not cursor is None:
    cursor.close()
if not db_connection is None:
    db_connection.close()