from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteDataHora
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters
from importersiconv.gerenciador_consultas import getIDConvenio

def salvarDesbloqueiosCR(arquivo_csv_desbloqueio_cr):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_desbloqueios_cr = 0
    with open(arquivo_csv_desbloqueio_cr, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            NR_CONVENIO = linha[0].strip()
            ID_CONVENIO = getIDConvenio(NR_CONVENIO)
            #Convênio não encontrado
            if ID_CONVENIO == 0:
                continue;
            NR_OB = linha[1].strip()
            DATA_CADASTRO = converteDataHora(linha[2].strip())
            DATA_ENVIO = converteDataHora(linha[3].strip())
            TIPO_RECURSO_DESBLOQUEIO = linha[4].strip()
            VL_TOTAL_DESBLOQUEIO = checarCampoVazio(linha[5].strip().replace(",", "."))
            VL_DESBLOQUEADO = checarCampoVazio(linha[6].strip().replace(",", "."))
            VL_BLOQUEADO = checarCampoVazio(linha[7].strip().replace(",", "."))

            sql = "INSERT INTO Desbloqueio_CR(ID_Convenio, Tipo_Recurso_Desbloqueio, Nr_OB, Data_Cadastro, \
                    Data_Envio, Valor_Total_Desbloqueio, Valor_Desbloqueado, Valor_Bloqueado) VALUES(" + str(ID_CONVENIO) + ", '" + \
                    str(TIPO_RECURSO_DESBLOQUEIO) + "', '" + str(NR_OB) + "', " + str(DATA_CADASTRO) + ", " + str(DATA_ENVIO) + ", " + \
                    str(VL_TOTAL_DESBLOQUEIO) + ", " + str(VL_DESBLOQUEADO) + ", " + str(VL_BLOQUEADO) + ")"
            
            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_desbloqueios_cr = numero_desbloqueios_cr + 1
            except Exception as e:
                print("Erro ao gravar Desbloqueio CR  %s" % (NR_OB))
                print(str(e))
                print(sql)
                break
        
    
    print("Gravadas %d Desqloqueios CR" % (numero_desbloqueios_cr)) 
