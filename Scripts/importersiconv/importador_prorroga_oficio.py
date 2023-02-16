from csv import reader
import mysql.connector
#from database.gerenciador_conexao_bd import connect
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio
from importersiconv.gerenciador_consultas import getIDConvenio

def salvarProrrogaOficio(arquivo_csv_prorroga_oficio):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_prorroga_oficio = 0
    with open(arquivo_csv_prorroga_oficio, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            NR_CONVENIO = linha[0].strip()
            #Sem número do convênio
            if NR_CONVENIO == "":
                continue;
            ID_CONVENIO = getIDConvenio(NR_CONVENIO)
            #Convênio não encontrado
            if ID_CONVENIO == 0:
                continue;
            NR_PRORROGA = linha[1].strip()
            DT_INICIO_PRORROGA = converteData(linha[2].strip())
            DT_FIM_PRORROGA = converteData(linha[3].strip())
            DIAS_PRORROGA = checarCampoVazio(linha[4].strip())
            DT_ASSINATURA_PRORROGA = converteData(linha[5].strip())
            SIT_PRORROGA = linha[6].strip()

            sql = "INSERT INTO Prorroga_Oficio(ID_Convenio, Situacao_Prorroga, Nr_Prorroga, Data_Inicio_Prorroga, \
                    Data_Fim_Prorroga, Dias_Prorroga, Data_Assinatura_Prorroga) VALUES(" + str(ID_CONVENIO) + ", '" + \
                    str(SIT_PRORROGA) + "', '" + str(NR_PRORROGA) + "', " + str(DT_INICIO_PRORROGA) + ", " + \
                    str(DT_FIM_PRORROGA) + ", " + str(DIAS_PRORROGA) + ", " + str(DT_ASSINATURA_PRORROGA) + ")"
            
            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_prorroga_oficio = numero_prorroga_oficio + 1
            except Exception as e:
                print("Erro ao gravar Prorrogação de Ofício %s" % (NR_PRORROGA))
                print(str(e))
                continue
        
    
    print("Gravadas %d Prorrogações de Ofício" % (numero_prorroga_oficio))