from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters
from importersiconv.gerenciador_consultas import getIDProposta

#Grava os empenhos do Mapa no banco de dados
def salvarEmendas(arquivo_csv_emendas):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_emendas = 0
    with open(arquivo_csv_emendas, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            ID_PROPOSTA = linha[0].strip()
            #Não gravo a Emenda, caso não haja proposta
            if ID_PROPOSTA == '':
                continue
            ID_PROPOSTA = getIDProposta(ID_PROPOSTA)
            #Não gravo a emenda, caso ela não tenha sido inserida. Provavelmente, não é do MAPA
            if ID_PROPOSTA == 0:
                continue
            QUALIF_PROPONENTE = linha[1].strip()
            COD_PROGRAMA_EMENDA = linha[2].strip()
            NR_EMENDA = linha[3].strip()
            NOME_PARLAMENTAR = removeNonASCIICharacters(linha[4].strip()).replace("'", "\\'")
            BENEFICIARIO_EMENDA = removeNonASCIICharacters(linha[5].strip()).replace("'", "\\'")
            IND_IMPOSITIVO = linha[6].strip()
            TIPO_PARLAMENTAR = linha[7].strip()
            VALOR_REPASSE_PROPOSTA_EMENDA = checarCampoVazio(linha[8].strip().replace(",", "."))
            VALOR_REPASSE_EMENDA = checarCampoVazio(linha[9].strip().replace(",", "."))

            sql = "INSERT INTO Emenda(ID_Proposta, Qualif_Proponente, Cod_Programa_Emenda, Nr_Emenda, \
                Nome_Parlamentar, Beneficiario_Emenda, Ind_Imposititvo, Tipo_Parlamentar, \
                Valor_Repasse_Proposta_Emenda, Valor_Repasse_Emenda) VALUES(%s, '%s', '%s', '%s', \
                '%s', '%s', '%s', '%s', %s, %s)" % (ID_PROPOSTA, QUALIF_PROPONENTE, COD_PROGRAMA_EMENDA, \
                NR_EMENDA, NOME_PARLAMENTAR, BENEFICIARIO_EMENDA, IND_IMPOSITIVO, TIPO_PARLAMENTAR, \
                VALOR_REPASSE_PROPOSTA_EMENDA, VALOR_REPASSE_EMENDA)
            
            try:
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                db_connection.commit()
                numero_emendas = numero_emendas + 1
            except Exception as e:
                print("Erro ao atualizar Emenda da Proposta %s" % ID_PROPOSTA)
                print(sql)
                print(str(e))
                break
        
    
    print("Atualizadas %d Emendas" % (numero_emendas)) 