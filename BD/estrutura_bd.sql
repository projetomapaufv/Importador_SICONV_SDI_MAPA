Create Database Convenios_Mapa;

Create Table Propostas_SDI_MAPA
(
	Codigo_Proposta INT
)

Create Table Proponente 
(
	ID_Proponente INT NOT NULL AUTO_INCREMENT,
    CNPJ Char(14),
    Nome Varchar(300),
    Municipio Varchar(100),
    UF Char(2),
    Endereco Varchar(300),
    Bairro Varchar(100),
    CEP Varchar(10),
    Email Varchar(100),
    Telefone Varchar(100),
    Fax Varchar(100),
    
    PRIMARY KEY(ID_Proponente)
);

Create Table Proposta
(
	ID_Proposta INT NOT NULL AUTO_INCREMENT,
    ID_Proponente INT, 
    Modalidade_Proposta Varchar(100), 
    Situacao_Conta Varchar(100), 
    Situacao_Projeto_Basico Varchar(100), 
    Situacao_Proposta Varchar(100), 
    Codigo_Proposta INT, /*ID da Proposta no Siconv*/
    UF_Proponente Char(2),
    Municipio_Proponente Varchar(100),
    Cod_Municipio_IBGE INT,
    Cod_Orgao_Superior INT, 
    Desc_Orgao_Superior Varchar(200),
	Natureza_Juridica Varchar(200),
    Nr_Proposta Varchar(30),
    Data_Proposta Date,
    Cod_Orgao INT, 
    Desc_Orgao Varchar(200),
    Nome_Proponente Varchar(300),
    CEP_Proponente Varchar(10),
    Endereco_Proponente Varchar(300),
    Bairro_Proponente Varchar(100),
    Nome_Banco Varchar(100),
    Data_Inicio_Vigencia Date,
    Data_Fim_Vigencia Date,
    Objeto_Proposta Text,
    Item_Investimento Text,
    Enviada_Mandataria Varchar(20),
    Valor_Global_Proposta Decimal(15,2),
    Valor_Repasse_Proposta Decimal(15,2),
    Valor_Contrapartida_Proposta Decimal(15,2),
    
    PRIMARY KEY(ID_Proposta),
    FOREIGN KEY (ID_Proponente) REFERENCES Proponente(ID_Proponente)
);

Create Table Justificativa_Proposta
(
	ID_Justificativa_Proposta INT NOT NULL AUTO_INCREMENT,
    ID_Proposta INT NOT NULL, /*Foreign Key*/
    Caracterizacao_Interesses_Reciprocos Text,
    Publico_Alvo Text,
    Problema_A_Ser_Resolvido Text,
    Resultados_Esperados Text,
    Relacao_Proposta_Objetivos_Programa Text,
    Capacidade_Tecnica Text,
    
    PRIMARY KEY(ID_Justificativa_Proposta),
    FOREIGN KEY (ID_Proposta) REFERENCES Proposta(ID_Proposta)
);

Create Table Convenio
(
	ID_Convenio INT NOT NULL AUTO_INCREMENT,
    Nr_Convenio INT NOT NULL UNIQUE,
    ID_Proposta INT NOT NULL, /*Foreign Key*/
    Situacao_Convenio Varchar(100), 
    Subsituacao_Convenio Varchar(100), 
    Situacao_Publicacao_Convenio Varchar(100), 
    Situacao_Contratacao_Convenio Varchar(100), 
    Codigo_Convenio_Siconv INT, /*ID do Convênio no Siconv*/
    Data_Assinatura Date,
    Instrumento_Ativo Boolean, 
    Ind_Opera_OBTV Boolean,
    Nr_Processo Varchar(50),
    UG_Emitente Varchar(20),
    Data_Publicacao Date,
    Data_Inicio_Vigencia Date,
    Data_Fim_Vigencia Date,
    Data_Fim_Vigencia_Original Date,
    Dias_Prestacao_Contas Int,
    Data_Limite_Prestacao_Contas Date,
    Data_Clausula_Suspensiva Date,
    Data_Retirada_Clausula_Suspensiva Date,
    Dias_Clausula_Suspensiva Int,
    Ind_Assinado Boolean,
    Motivo_Suspensao Text,
    Ind_Foto Boolean,
    Qtde_Convenios Int,
    Qtde_TA Int,
    Qtde_Prorroga Int,
    Valor_Global_Convenio Decimal(15,2),
    Valor_Repasse_Convenio Decimal(15,2),
    Valor_Contrapartida_Convenio Decimal(15,2),
    Valor_Empenhado_Convenio Decimal(15,2),
    Valor_Desembolsado_Convenio Decimal(15,2),
    Valor_Saldo_Reman_Tesouro Decimal(15,2),
	Valor_Saldo_Reman_Convenente Decimal(15,2),
    Valor_Rendimento_Aplicacao Decimal(15,2),
    Valor_Ingresso_Contrapartida Decimal(15,2),
    Valor_Saldo_Conta Decimal(15,2),
    Valor_Global_Original_Convenio Decimal(15,2),
    
    PRIMARY KEY(ID_Convenio),
    FOREIGN KEY (ID_Proposta) REFERENCES Proposta(ID_Proposta)
);

Create Table Licitacao
(
	ID_Licitacao INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Modalidade_Licitacao Varchar(100), 
    Tipo_Processo_Compra Varchar(100), 
    Tipo_Licitacao Varchar(100), 
	Status_Licitacao Varchar(100),
    Codigo_Licitacao_Siconv INT, /*ID da Licitação no Siconv*/
    Nr_Licitacao Varchar(200),
    Nr_Processo_Licitacao Varchar(200),
    Data_Publicacao_Licitacao Date,
	Data_Abertura_Licitacao Date,
    Data_Encerramento_Licitacao Date,
    Data_Homologacao_Licitacao Date, 
    Situacao_Aceite_Processo_Execucao Varchar(50),
    Sistema_Origem Varchar(200),
    Situacao_Sistema Varchar(50),
    Valor_Licitacao Decimal(15,2),
    
    Primary Key (ID_Licitacao),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Empenho 
(
	ID_Empenho INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Descricao_Tipo_Nota Varchar(100), 
    Descricao_Situacao_Empenho Varchar(100), 
    Codigo_Empenho_Siconv INT, /*Código do Empenho no Siconv*/
    Nr_Empenho Varchar(20),
    Tipo_Nota INT,
    Data_Emissao Date,
    Codigo_Situacao_Empenho INT, /*Tratar os casos em que tem o texto ENVIADO. ENVIADO = 4*/
    Valor_Empenhado Decimal(15,2),
    
    Primary Key(ID_Empenho),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Pagamento_Tributo
(
	ID_Pagamento_Tributo INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Codigo_Pagamento_Tributo_Siconv INT, /*ID do Pagamento de Tributo no Siconv*/
    Data_Tributo Date,
    Valor_Pago_Tributo Decimal(15,2),
    
    Primary Key(ID_Pagamento_Tributo),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Prorroga_Oficio
(
	ID_Prorroga_Oficio INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Situacao_Prorroga Varchar(100),
    Nr_Prorroga Varchar(200),
    Data_Inicio_Prorroga Date,
    Data_Fim_Prorroga Date,
    Dias_Prorroga INT,
    Data_Assinatura_Prorroga Date,
    
    Primary Key(ID_Prorroga_Oficio),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Termo_Aditivo
(
	ID_Termo_Aditivo INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Codigo_Termo_Aditivo_Siconv INT, /*Id do termo aditivo no Siconv*/
    Numero_TA Varchar(50),
    Tipo_TA Varchar(100),
    Valor_Global_TA Decimal(15,2),
    Valor_Repasse_TA Decimal(15,2),
    Valor_Contrapartida_TA Decimal(15,2),
    Data_Assinatura_TA Date, 
    Data_Inicio_TA Date,
    Data_Fim_TA Date, 
    Justificativa_TA Text,
    
    Primary Key(ID_Termo_Aditivo),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Meta_Crono_Fisico
(
	ID_Meta_Crono_Fisico INT NOT NULL AUTO_INCREMENT,
    ID_Proposta INT NOT NULL, /*Foreign Key*/
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Tipo_Meta Varchar(100),
    Codigo_Meta_Crono_Fisico INT, /*ID da Meta no Siconv*/ 
    Cod_Programa Varchar(20),
    Nome_Programa Varchar(1000),
    Nr_Meta Varchar(20),
    Descricao_Meta Text,
    Data_Inicio_Meta Date, 
    Data_Fim_Meta Date, 
    UF_Meta Char(2),
    Municipio_Meta Varchar(100),
    Endereco_Meta Varchar(300),
	CEP_Meta Varchar(20),
    Qtde_Meta Varchar(50),
    Unidade_Fornecimento_Meta Varchar(100), /*Checar o Tipo*/
    Valor_Meta Decimal(15,2),
    
    Primary Key(ID_Meta_Crono_Fisico),
    FOREIGN KEY (ID_Proposta) REFERENCES Proposta(ID_Proposta),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Etapa_Crono_Fisico
(
	ID_Etapa_Crono_Fisico INT NOT NULL AUTO_INCREMENT,
    ID_Meta_Crono_Fisico INT, /*Foreign Key*/
    Codigo_Etapa INT, /*ID da Etapa no Siconv*/ 
    Nr_Etapa INT, 
    Descricao_Etapa Varchar(1000),
    Data_Inicio_Etapa Date,
    Data_Fim_Etapa Date,
    UF_Etapa Char(2),
    Municipio_Etapa Varchar(100),
    Endereco_Etapa Varchar(300),
    CEP_Etapa Varchar(20),
    Qtde_Etapa Varchar(50),
    Unidade_Fornecimento_Etapa Varchar(100),
    
    Primary Key (ID_Etapa_Crono_Fisico),
    FOREIGN KEY (ID_Meta_Crono_Fisico) REFERENCES Meta_Crono_Fisico(ID_Meta_Crono_Fisico)
);

Create Table Ingresso_Contrapartida
(
	ID_Ingresso_Contrapartida INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL,
    Data_Ingresso_Contrapartida Date,
    Valor_Ingresso_Contrapartida Decimal(15,2),
    
    primary key (ID_Ingresso_Contrapartida),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Desembolso 
(
	ID_Desembolso INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Codigo_Desembolso_Siconv INT, /*ID do Desembolso no Siconv*/ 
    Data_Ultimo_Desembolso Date, 
    Qtde_Dias_Sem_Desembolso INT, 
    Data_Desembolso Date,
    Nr_SIAFI Varchar(50),
    Valor_Desembolsado Decimal(15,2),
    
    Primary Key(ID_Desembolso),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Empenho_Desembolso
(
	ID_Empenho_Desembolso INT NOT NULL AUTO_INCREMENT,
    ID_Empenho INT, /*Foreign Key*/
    ID_Desembolso INT, /*Foreign Key*/
    Valor_Grupo Decimal(15,2),
    
    Primary Key(ID_Empenho_Desembolso),
    FOREIGN KEY (ID_Empenho) REFERENCES Empenho(ID_Empenho),
    FOREIGN KEY (ID_Desembolso) REFERENCES Desembolso(ID_Desembolso)
);

Create Table Pagamento
(
	ID_Pagamento INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Tipo_Movimentacao_Financeira Varchar(100), 
    Descricao_DL Varchar(100),
    Nr_Movimentacao_Financeira INT, 
    Identificacao_Fornecedor Varchar(50),
    Nome_Fornecedor Varchar(300),
    Data_Pagamento Date,
	Nr_DL Varchar(20),
    Valor_Pago Decimal(15,2),
    
	Primary Key(ID_Pagamento),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table OBTV_Convenente
(
	ID_OBTV_Convenente INT NOT NULL AUTO_INCREMENT,
    ID_Pagamento INT, /*Foreign Key*/
    Identificacao_Favorecido_OBTV_Convenente Varchar(20),
    Nome_Favorecido_OBTV_Convenente Varchar(200),
    Tipo_Aquisicao Varchar(100),
    Valor_Pago_OBTV_Convenente Decimal(15,2),
    
    Primary Key(ID_OBTV_Convenente),
    FOREIGN KEY (ID_Pagamento) REFERENCES Pagamento(ID_Pagamento)
);

Create Table Desbloqueio_CR
(
	ID_Desbloqueio_CR INT NOT NULL AUTO_INCREMENT,
    ID_Convenio INT NOT NULL, /*Foreign Key*/
    Tipo_Recurso_Desbloqueio Varchar(100),
    Nr_OB Varchar(30),
    Data_Cadastro Datetime,
    Data_Envio Datetime,
    Valor_Total_Desbloqueio Decimal(15,2),
    Valor_Desbloqueado Decimal(15,2),
    Valor_Bloqueado Decimal(15,2),
    
    Primary Key(ID_Desbloqueio_CR),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Cronograma_Desembolso
(
	ID_Cronograma_Desembolso INT NOT NULL AUTO_INCREMENT,
    ID_Proposta INT NOT NULL, /*Foreign Key*/
    ID_Convenio INT, /*Foreign Key*/
    Tipo_Responsavel_Cronograma_Desembolso Varchar(100), /*Foreign Key*/ 
    Nr_Parcela_Cronograma_Desembolso INT, 
    Mes_Cronograma_Desembolso INT, 
    Ano_Cronograma_Desembolso INT,
    Valor_Parcela_Desembolso Decimal(15,2),
    
    Primary Key(ID_Cronograma_Desembolso),
    FOREIGN KEY (ID_Proposta) REFERENCES Proposta(ID_Proposta),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Historico_Situacao
(
	ID_Historico_Situacao INT NOT NULL AUTO_INCREMENT,
    ID_Proposta INT NOT NULL,
    ID_Convenio INT,
    Data_Historico_Situacao datetime,
    Historico_Situacao Varchar(100),
    Dias_Historico_Situacao INT,
    Codigo_Historico_Situacao INT,
    
    Primary Key(ID_Historico_Situacao),
    FOREIGN KEY (ID_Proposta) REFERENCES Proposta(ID_Proposta),
    FOREIGN KEY (ID_Convenio) REFERENCES Convenio(ID_Convenio)
);

Create Table Ultima_Atualizacao_Dados
(
	Ultima_Atualizacao Datetime
);
