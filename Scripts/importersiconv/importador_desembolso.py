from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters
from importersiconv.gerenciador_consultas import getIDConvenio

def salvarDesembolsos(arquivo_csv_desembolso):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_desembolsos = 0
    with open(arquivo_csv_desembolso, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            ID_DESEMBOLSO = checarCampoVazio(linha[0].strip())
            NR_CONVENIO = linha[1].strip()
            ID_CONVENIO = getIDConvenio(NR_CONVENIO)
            #Convênio não encontrado
            if ID_CONVENIO == 0:
                continue;
            DT_ULT_DESEMBOLSO = converteData(linha[2].strip())
            QTD_DIAS_SEM_DESEMBOLSO = checarCampoVazio(linha[3].strip())
            DATA_DESEMBOLSO = converteData(linha[4].strip())
            #ANO_DESEMBOLSO = checarCampoVazio(linha[5].strip())
            #MES_DESEMBOLSO = checarCampoVazio(linha[6].strip())
            NR_SIAFI = linha[7].strip()
            VL_DESEMBOLSADO = checarCampoVazio(linha[8].strip().replace(",", "."))

            sql = "INSERT INTO Desembolso(ID_Convenio, Codigo_Desembolso_Siconv, Data_Ultimo_Desembolso, Qtde_Dias_Sem_Desembolso,\
                    Data_Desembolso, Nr_SIAFI, Valor_Desembolsado) VALUES(" + str(ID_CONVENIO) + ", " + str(ID_DESEMBOLSO) + ", " + \
                    str(DT_ULT_DESEMBOLSO) + ", " + str(QTD_DIAS_SEM_DESEMBOLSO) + ", " + str(DATA_DESEMBOLSO) + ", '" + str(NR_SIAFI) + "', " + \
                    str(VL_DESEMBOLSADO) + ")"
            
            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_desembolsos = numero_desembolsos + 1
            except Exception as e:
                print("Erro ao gravar Desembolso de %s do Convênio %s" % (VL_DESEMBOLSADO, NR_CONVENIO))
                print(str(e))
                print(sql)
                continue
        
    
    print("Gravadas %d Desembolsos" % (numero_desembolsos)) 
 