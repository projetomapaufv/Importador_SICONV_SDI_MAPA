from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters
from importersiconv.gerenciador_consultas import getIDPagamento

def salvarObtvConvenente(arquivo_csv_obtv_convenente):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_obtvs_convenente = 0
    with open(arquivo_csv_obtv_convenente, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            NR_MOV_FIN = linha[0].strip()
            ID_PAGAMENTO = getIDPagamento(NR_MOV_FIN)
            if ID_PAGAMENTO == 0:
                continue
            IDENTIF_FAVORECIDO_OBTV_CONV = linha[1].strip()
            NM_FAVORECIDO_OBTV_CONV = linha[2].strip()
            TP_AQUISICAO = linha[3].strip()
            VL_PAGO_OBTV_CONV = checarCampoVazio(linha[4].strip().replace(",", "."))

            sql = "INSERT INTO OBTV_Convenente(ID_PAGAMENTO, Identificacao_Favorecido_OBTV_Convenente, Nome_Favorecido_OBTV_Convenente, \
                    Tipo_Aquisicao, Valor_Pago_OBTV_Convenente) VALUES(" + str(ID_PAGAMENTO) + ", '" + str(IDENTIF_FAVORECIDO_OBTV_CONV) + "', '" + \
                    str(NM_FAVORECIDO_OBTV_CONV) + "', '" + str(TP_AQUISICAO) + "', " + str(VL_PAGO_OBTV_CONV) + ")"
            
            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_obtvs_convenente = numero_obtvs_convenente + 1
            except Exception as e:
                print("Erro ao gravar OBTV de %s com número de Movimentação %s" % (VL_PAGO_OBTV_CONV, NR_MOV_FIN))
                print(str(e))
                print(sql)
                continue
        
    
    print("Gravadas %d OBTVs" % (numero_obtvs_convenente)) 