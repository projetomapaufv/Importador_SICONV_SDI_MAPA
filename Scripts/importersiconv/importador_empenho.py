from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import connect
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio
from importersiconv.gerenciador_consultas import getIDConvenio

#Grava os empenhos do Mapa no banco de dados
def salvarEmpenhos(arquivo_csv_empenhos):
    db_connection = connect()

    numero_linhas_csv = 0
    numero_empenhos = 0
    with open(arquivo_csv_empenhos, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            ID_EMPENHO = linha[0].strip()
            NR_CONVENIO = linha[1].strip()
            #Sem número do convênio
            if NR_CONVENIO == "":
                continue;
            ID_CONVENIO = getIDConvenio(NR_CONVENIO)
            #Convênio não encontrado
            if ID_CONVENIO == 0:
                continue;
            NR_EMPENHO = linha[2].strip()
            TIPO_NOTA = linha[3].strip()
            DESC_TIPO_NOTA = linha[4].strip()
            DATA_EMISSAO = converteData(linha[5].strip())
            COD_SITUACAO_EMPENHO = linha[6].strip()
            if COD_SITUACAO_EMPENHO == 'ENVIADO':
                COD_SITUACAO_EMPENHO = '4';
            DESC_SITUACAO_EMPENHO = linha[7].strip()
            VALOR_EMPENHADO = checarCampoVazio(linha[8].strip().replace(",", "."))

            sql = "INSERT INTO Empenho(ID_Convenio, Descricao_Tipo_Nota, Descricao_Situacao_Empenho, \
                    Codigo_Empenho_Siconv, Nr_Empenho, Tipo_Nota, Data_Emissao, Codigo_Situacao_Empenho, \
                    Valor_Empenhado) VALUES(" + str(ID_CONVENIO) + ", '" + str(DESC_TIPO_NOTA) + "', '" + \
                    str(DESC_SITUACAO_EMPENHO) + "', " + str(ID_EMPENHO) + ", '" + str(NR_EMPENHO) + "', " + \
                    str(TIPO_NOTA) + ", " + str(DATA_EMISSAO) + ", " + str(COD_SITUACAO_EMPENHO) + ", " + \
                    str(VALOR_EMPENHADO) + ")"
            
            try:
                cursor = db_connection.cursor()
                cursor.execute(sql)
                cursor.close()
                db_connection.commit()
                numero_empenhos = numero_empenhos + 1
            except Exception as e:
                print("Erro ao gravar Empenho %s" % ID_EMPENHO)
                print(str(e))
                continue
        
    
    print("Gravados %d Empenhos" % (numero_empenhos)) 



    

