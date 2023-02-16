from csv import reader
import mysql.connector
from database.gerenciador_conexao_bd import Connection
from util.dateUtil import converteData
from util.stringUtil import checarCampoVazio, removeNonASCIICharacters
from importersiconv.gerenciador_consultas import getIDConvenio

def salvarPagamentos(arquivo_csv_pagamentos):
    db_connection = Connection.connect()

    numero_linhas_csv = 0
    numero_pagamentos = 0
    with open(arquivo_csv_pagamentos, 'r') as arquivo_csv:
        csv_reader = reader(arquivo_csv, delimiter=';')
        for linha in csv_reader:
            ##Leitura dos dados da planilha
            if numero_linhas_csv == 0:
                numero_linhas_csv = numero_linhas_csv + 1
                continue
            numero_linhas_csv = numero_linhas_csv + 1
            #Campos do CSV
            NR_MOV_FIN = linha[0].strip()
            NR_CONVENIO = linha[1].strip()
            ID_CONVENIO = getIDConvenio(NR_CONVENIO)
            #Convênio não encontrado
            if ID_CONVENIO == 0:
                continue;
            IDENTIF_FORNECEDOR = linha[2].strip()
            NOME_FORNECEDOR = removeNonASCIICharacters(linha[3].strip().replace("'", "\\'"))
            TP_MOV_FINANCEIRA = linha[4].strip()
            DATA_PAG = converteData(linha[5].strip())
            NR_DL = linha[6].strip()
            DESC_DL = linha[7].strip()
            VL_PAGO = checarCampoVazio(linha[8].strip().replace(",", "."))

            sql = "INSERT INTO Pagamento(ID_Convenio, Tipo_Movimentacao_Financeira, Descricao_DL, Nr_Movimentacao_Financeira,  \
                    Identificacao_Fornecedor, Nome_Fornecedor, Data_Pagamento, Nr_DL, Valor_Pago) VALUES(" + str(ID_CONVENIO) + ", '" + \
                    str(TP_MOV_FINANCEIRA) + "', '" + str(DESC_DL) + "', '" + str(NR_MOV_FIN) + "', '" + str(IDENTIF_FORNECEDOR) + "', '" + \
                    str(NOME_FORNECEDOR) + "', " + str(DATA_PAG) + ", '" + str(NR_DL) + "', " + str(VL_PAGO) + ")"
            
            try:
                 #cursor = db_connection.cursor()
                db_connection = Connection.connect()
                cursor = Connection.getCursor()
                cursor.execute(sql)
                #cursor.close()
                db_connection.commit()
                numero_pagamentos = numero_pagamentos + 1
            except Exception as e:
                print("Erro ao gravar Pagamento %s" % (NR_MOV_FIN))
                print(str(e))
                print(sql)
                break
        
    
    print("Gravadas %d Pagamentos" % (numero_pagamentos)) 