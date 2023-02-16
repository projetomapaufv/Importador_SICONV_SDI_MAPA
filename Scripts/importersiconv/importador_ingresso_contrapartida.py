from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters
from importersiconv.gerenciador_consultas import getIDConvenio

def salvarIngressosContrapartida(arquivo_csv_ingresso_contrapartida):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_ingressos_contrapartida = 0
    with open(arquivo_csv_ingresso_contrapartida, 'r') as arquivo_csv:
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
            DT_INGRESSO_CONTRAPARTIDA = converteData(linha[1].strip())
            VL_INGRESSO_CONTRAPARTIDA = checarCampoVazio(linha[2].strip().replace(",", "."))

            sql = "INSERT INTO Ingresso_Contrapartida(ID_Convenio, Data_Ingresso_Contrapartida, Valor_Ingresso_Contrapartida) \
                    VALUES(" + str(ID_CONVENIO) + ", " + str(DT_INGRESSO_CONTRAPARTIDA) + ", " + str(VL_INGRESSO_CONTRAPARTIDA) + ")"
            
            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_ingressos_contrapartida = numero_ingressos_contrapartida + 1
            except Exception as e:
                print("Erro ao gravar Ingresso de Contrapartida de %s do Convênio %s" % (DT_INGRESSO_CONTRAPARTIDA, NR_CONVENIO))
                print(str(e))
                print(sql)
                continue
        
    
    print("Gravadas %d Ingressos de Contrapartida" % (numero_ingressos_contrapartida)) 