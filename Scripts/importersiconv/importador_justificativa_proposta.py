from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import connect
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio
from importersiconv.gerenciador_consultas import getIDConvenio

def salvarJustificativas(arquivo_csv_justificativas):
    numero_linhas_csv = 0
    numero_justificativas = 0
    with open(arquivo_csv_justificativas, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            
