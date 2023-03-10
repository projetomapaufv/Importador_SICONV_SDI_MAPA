#!/usr/bin/env python
# -*- coding: utf-8 -*-
from database.gerenciador_conexao_bd import Connection
from importermatrizmapa.importador_matriz_mapa import salvarMatrizMapa

ARQUIVO_MATRIZ_MAPA = '/home/vagner/Projeto_MAPA/MATRIZ-27-02-2023.csv'

salvarMatrizMapa(ARQUIVO_MATRIZ_MAPA)

#Fecho a conexão
db_connection = Connection.getConnection()
cursor = Connection.getCursor()
if not cursor is None:
    cursor.close()
if not db_connection is None:
    db_connection.close()