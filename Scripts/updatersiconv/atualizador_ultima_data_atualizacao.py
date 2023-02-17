from csv import reader
import mysql.connector
#from database.gerenciador_conexao_bd import connect
from database.gerenciador_conexao_bd import Connection
from datetime import date, datetime
from importersiconv.gerenciador_consultas import getIDProposta
from util.stringUtil import checarCampoVazio
from util.dateUtil import converteDataHora

def atualizarUltimaDataAtualizacao(arquivo_csv_data_atualizacao):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    with open(arquivo_csv_data_atualizacao, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            #Pula a primeira linha - Título da coluna
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            
            DATA_CARGA = converteDataHora(linha[0].strip())
            if DATA_CARGA == 'NULL':
                print("Erro ao atualizar a data da última atualização dos dados")
                return
            
            sql = 'UPDATE Ultima_Atualizacao_Dados SET Ultima_Atualizacao = ' + DATA_CARGA
            try:
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                db_connection.commit()
            except Exception as e:
                print("Erro ao salvar última atualização dos dados")
                print(str(e))
                return
    
    print("Última atualização dos dados gravada com sucesso!") 