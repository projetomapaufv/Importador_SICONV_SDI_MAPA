from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio
from importersiconv.gerenciador_consultas import getIDProposta
from util.stringUtil import removeNonASCIICharacters

def salvarJustificativasPropostas(arquivo_csv_justificativas):
    #db_connection = Connection.connect()

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
            ID_PROPOSTA = linha[0].strip()
            ID_PROPOSTA = getIDProposta(ID_PROPOSTA)
            #Proposta não encontrada
            if ID_PROPOSTA == 0:
                continue;
            CARACTERIZACAO_INTERESSES_RECI = removeNonASCIICharacters(linha[1].strip()).replace("'", "\\'")        
            PUBLICO_ALVO = removeNonASCIICharacters(linha[2].strip()).replace("'", "\\'")
            PROBLEMA_A_SER_RESOLVIDO = removeNonASCIICharacters(linha[3].strip()).replace("'", "\\'")
            RESULTADOS_ESPERADOS = removeNonASCIICharacters(linha[4].strip()).replace("'", "\\'")
            RELACAO_PROPOSTA_OBJETIVOS_PRO = removeNonASCIICharacters(linha[5].strip()).replace("'", "\\'")
            CAPACIDADE_TECNICA = removeNonASCIICharacters(linha[6].strip()).replace("'", "\\'")
            JUSTIFICATIVA = removeNonASCIICharacters(linha[7].strip()).replace("'", "\\'")

            sql = "INSERT INTO Justificativa_Proposta(ID_Proposta, Caracterizacao_Interesses_Reciprocos, Publico_Alvo, \
                    Problema_A_Ser_Resolvido, Resultados_Esperados, Relacao_Proposta_Objetivos_Programa, Capacidade_Tecnica) \
                    VALUES(" + str(ID_PROPOSTA) + ", '" + str(CARACTERIZACAO_INTERESSES_RECI) + "', '" + str(PUBLICO_ALVO) + "', '" + \
                    str(PROBLEMA_A_SER_RESOLVIDO) + "', '" + str(RESULTADOS_ESPERADOS) + "', '" + str(RELACAO_PROPOSTA_OBJETIVOS_PRO) + "', '" + \
                    str(CAPACIDADE_TECNICA) + "')"
            try:
                #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_justificativas = numero_justificativas + 1
            except Exception as e:
                print("Erro ao gravar Justificativas da Proposta %s" % ID_PROPOSTA)
                print(sql)
                print(str(e))
                break
        
    
    print("Gravadas %d Justificativas de Proposta" % (numero_justificativas))

