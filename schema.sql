CREATE TABLE PESSOA (
    CPF CHAR(14) NOT NULL,
    NOME VARCHAR(128) NOT NULL,
    EMAIL VARCHAR(64),
    ENDERECO VARCHAR(128),
    CONSTRAINT PK_PESSOA_0 PRIMARY KEY (CPF),
    CONSTRAINT CK_PESSOA_0 CHECK(CPF ~ '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'),
    CONSTRAINT CK_PESSOA_1 CHECK (EMAIL ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z.]+$')
);

CREATE TABLE CLIENTE (
    CPF CHAR(14) NOT NULL,
    CONSTRAINT PK_CLIENTE_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_CLIENTE_0 FOREIGN KEY (CPF)
        REFERENCES PESSOA (CPF)
        ON DELETE CASCADE
);
  
CREATE TABLE FUNCIONARIO (
    CPF CHAR(14) NOT NULL,
    SALARIO REAL NOT NULL,
    FUNCAO VARCHAR(32) NOT NULL,
    CONSTRAINT PK_FUNCIONARIO_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_FUNCIONARIO_0 FOREIGN KEY (CPF)
        REFERENCES PESSOA (CPF)
        ON DELETE CASCADE,
    CONSTRAINT CK_FUNCIONARIO_0 CHECK (SALARIO > 0.0)
);

CREATE TABLE ESPECIALISTA (
    CPF CHAR(14) NOT NULL,
    ESPECIALIDADE VARCHAR(32) NOT NULL,
    TAXA_HORA REAL NOT NULL,
    CONSTRAINT PK_ESPECIALISTA_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_ESPECIALISTA_0 FOREIGN KEY (CPF)
        REFERENCES PESSOA (CPF)
        ON DELETE CASCADE,
    CONSTRAINT CK_ESPECIALISTA_0 CHECK(
        TAXA_HORA > 0.0
    )
);

CREATE TABLE CONTRATO_ESPECIALISTA (
    ESPECIALISTA CHAR(14) NOT NULL,
    DATA_INICIO DATE NOT NULL,
    DURACAO INTEGER NOT NULL,
    REMUNERACAO REAL NOT NULL,
    CONSTRAINT PK_CONTRATO_ESPECIALISTA_0 PRIMARY KEY (ESPECIALISTA, DATA_INICIO),
    CONSTRAINT FK_CONTRATO_ESPECIALISTA_0 FOREIGN KEY (ESPECIALISTA)
        REFERENCES ESPECIALISTA (CPF)
        ON DELETE CASCADE,
    CONSTRAINT CK_CONTRATO_ESPECIALISTA_0 CHECK(
        REMUNERACAO >= 0.0
    )
);

CREATE TABLE BARTENDER (
    CPF CHAR(14) NOT NULL,
    CONSTRAINT PK_BARTENDER_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_BARTENDER_0 FOREIGN KEY (CPF)
        REFERENCES ESPECIALISTA (CPF)
        ON DELETE CASCADE
);

CREATE TABLE COPEIRO (
    CPF CHAR(14) NOT NULL,
    CONSTRAINT PK_COPEIRO_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_COPEIRO_0 FOREIGN KEY (CPF)
        REFERENCES ESPECIALISTA (CPF)
        ON DELETE CASCADE
);

CREATE TABLE CHEF (
    CPF CHAR(14) NOT NULL,
    CONSTRAINT PK_CHEF_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_CHEF_0 FOREIGN KEY (CPF)
        REFERENCES ESPECIALISTA (CPF)
        ON DELETE CASCADE
);

CREATE TABLE MAITRE (
    CPF CHAR(14) NOT NULL,
    CONSTRAINT PK_MAITRE_0 PRIMARY KEY (CPF),
    CONSTRAINT FK_MAITRE_0 FOREIGN KEY (CPF)
        REFERENCES ESPECIALISTA (CPF)
        ON DELETE CASCADE
);

CREATE TABLE TELEFONES (
    PESSOA CHAR(14) NOT NULL,
    TELEFONE VARCHAR(16) NOT NULL,
    CONSTRAINT PK_TELEFONES_0 PRIMARY KEY (PESSOA, TELEFONE),
    CONSTRAINT FK_TELEFONES_0 FOREIGN KEY (PESSOA)
        REFERENCES PESSOA (CPF)
        ON DELETE CASCADE,
    CONSTRAINT CK_TELEFONES_0 CHECK(TELEFONE ~* '^(\([0-9]{2}\) [0-9]{5}-[0-9]{4})|(\([0-9]{2}\) [0-9]{4}-[0-9]{4})$')
);

CREATE TABLE EVENTO (
    CLIENTE CHAR(14) NOT NULL,
    DATAHORA TIMESTAMP (0) NOT NULL,
    CATEGORIA VARCHAR(16) NOT NULL,
    VALOR REAL,
    METODOPAGAMENTO VARCHAR(16),
    NROPESSOAS INTEGER,
    CONSTRAINT PK_EVENTO_0 PRIMARY KEY (CLIENTE, DATAHORA),
    CONSTRAINT FK_EVENTO_0 FOREIGN KEY (CLIENTE)
        REFERENCES CLIENTE (CPF)
        ON DELETE CASCADE,
    CONSTRAINT CK_EVENTO_0 CHECK(
        UPPER(CATEGORIA) IN('CASAMENTO', 'FORMATURA')),
    CONSTRAINT CK_EVENTO_1 CHECK(
        NROPESSOAS >= 0),
    CONSTRAINT CK_EVENTO_2 CHECK(
        VALOR > 0.0 OR VALOR IS NULL)
);

CREATE TABLE FUNCIONARIO_EVENTO (
    FUNCIONARIO CHAR(14) NOT NULL,
    CLIENTE CHAR(14) NOT NULL,
    DATAHORA TIMESTAMP (0) NOT NULL,
    CONSTRAINT PK_FUNCIONARIO_EVENTO_0 PRIMARY KEY (FUNCIONARIO, CLIENTE, DATAHORA),
    CONSTRAINT FK_FUNCIONARIO_EVENTO_0 FOREIGN KEY (FUNCIONARIO)
        REFERENCES FUNCIONARIO (CPF)
        ON DELETE CASCADE,
    CONSTRAINT FK_FUNCIONARIO_EVENTO_1 FOREIGN KEY (CLIENTE, DATAHORA)
        REFERENCES EVENTO (CLIENTE, DATAHORA)
        ON DELETE CASCADE
);

CREATE TABLE LOCAL (
    ID BIGSERIAL NOT NULL,
    CEP VARCHAR(16) NOT NULL,
    NUMERO INTEGER NOT NULL,
    COMPLEMENTO VARCHAR(32),
    RUA VARCHAR(32) NOT NULL,
    CIDADE VARCHAR(32) NOT NULL,
    CAPACIDADE INTEGER,
    TIPO VARCHAR(16) NOT NULL,
    CONSTRAINT PK_LOCAL_0 PRIMARY KEY (ID),
    CONSTRAINT UK_LOCAL_0 UNIQUE (CEP, NUMERO, COMPLEMENTO),
    CONSTRAINT CK_LOCAL_0 CHECK(
        UPPER(TIPO) IN('SALAO', 'CAMPO')),
    CONSTRAINT CK_LOCAL_1 CHECK(
        CEP ~ '^[0-9]{5}\-[0-9]{3}$'),
    CONSTRAINT CK_LOCAL_2 CHECK(
        NUMERO > 0),
    CONSTRAINT CK_LOCAL_3 CHECK(
        CAPACIDADE >=0 OR CAPACIDADE IS NULL)
);

CREATE TABLE SALAO (
    ID BIGINT NOT NULL,
    CONSTRAINT PK_SALAO_0 PRIMARY KEY (ID),
    CONSTRAINT FK_SALAO_0 FOREIGN KEY (ID)
        REFERENCES LOCAL (ID) 
        ON DELETE CASCADE
);

CREATE TABLE CAMPO (
    ID BIGINT NOT NULL,
    CONSTRAINT PK_CAMPO_0 PRIMARY KEY (ID),
    CONSTRAINT FK_CAMPO_0 FOREIGN KEY (ID)
        REFERENCES LOCAL (ID)
        ON DELETE CASCADE
);

CREATE TABLE FORMATURA (
    CLIENTE CHAR(14) NOT NULL,
    DATAHORA TIMESTAMP (0) NOT NULL,
    BARTENDER CHAR(14),
    COPEIRO CHAR(14),
    SALAO BIGINT,
    CONSTRAINT PK_FORMATURA_0 PRIMARY KEY (CLIENTE, DATAHORA),
    CONSTRAINT FK_FORMATURA_0 FOREIGN KEY (CLIENTE, DATAHORA)
        REFERENCES EVENTO (CLIENTE, DATAHORA)
        ON DELETE CASCADE,
    CONSTRAINT FK_FORMATURA_1 FOREIGN KEY (BARTENDER)
        REFERENCES BARTENDER (CPF)
        ON DELETE SET NULL,
    CONSTRAINT FK_FORMATURA_2 FOREIGN KEY (COPEIRO)
        REFERENCES COPEIRO (CPF)
        ON DELETE SET NULL,
    CONSTRAINT FK_FORMATURA_3 FOREIGN KEY (SALAO)
        REFERENCES SALAO (ID)
        ON DELETE SET NULL
);

CREATE TABLE CASAMENTO (
    CLIENTE CHAR(14) NOT NULL,
    DATAHORA TIMESTAMP (0) NOT NULL,
    CHEF CHAR(14),
    MAITRE CHAR(14),
    LOCAL BIGINT,
    CONSTRAINT PK_CASAMENTO_0 PRIMARY KEY (CLIENTE, DATAHORA),
    CONSTRAINT FK_CASAMENTO_0 FOREIGN KEY (CLIENTE, DATAHORA)
        REFERENCES EVENTO (CLIENTE, DATAHORA)
        ON DELETE CASCADE,
    CONSTRAINT FK_CASAMENTO_1 FOREIGN KEY (CHEF)
        REFERENCES CHEF (CPF)
        ON DELETE SET NULL,
    CONSTRAINT FK_CASAMENTO_2 FOREIGN KEY (MAITRE)
        REFERENCES MAITRE (CPF)
        ON DELETE SET NULL,
    CONSTRAINT FK_CASAMENTO_3 FOREIGN KEY (LOCAL)
        REFERENCES LOCAL (ID)
        ON DELETE SET NULL
);

CREATE TABLE CARDAPIO (
    CLIENTE CHAR(14) NOT NULL,
    DATAHORA TIMESTAMP (0) NOT NULL,
    NROITEMS INTEGER NOT NULL,
    CONSTRAINT PK_CARDAPIO_0 PRIMARY KEY (CLIENTE, DATAHORA),
    CONSTRAINT FK_CARDAPIO_0 FOREIGN KEY (CLIENTE, DATAHORA)
        REFERENCES EVENTO (CLIENTE, DATAHORA)
        ON DELETE CASCADE,
    CONSTRAINT FK_CARDAPIO_1 CHECK(
        NROITEMS > 0)
);

CREATE TABLE ITEM (
    NOME VARCHAR(32) NOT NULL,
    CONSTRAINT PK_ITEM_0 PRIMARY KEY (NOME)
);

CREATE TABLE CARDAPIO_ITEM (
    CLIENTE CHAR(14) NOT NULL,
    DATAHORA TIMESTAMP (0) NOT NULL,
    ITEM VARCHAR(32) NOT NULL,
    CONSTRAINT PK_CARDAPIO_ITEM_0 PRIMARY KEY (CLIENTE, DATAHORA, ITEM),
    CONSTRAINT FK_CARDAPIO_ITEM_0 FOREIGN KEY (CLIENTE, DATAHORA)
        REFERENCES EVENTO (CLIENTE, DATAHORA)
        ON DELETE CASCADE,
    CONSTRAINT FK_CARDAPIO_ITEM_1 FOREIGN KEY (ITEM)
        REFERENCES ITEM (NOME)
        ON DELETE CASCADE
);

CREATE TABLE INGREDIENTES (
    ITEM VARCHAR(32) NOT NULL,
    NOME VARCHAR(32) NOT NULL,
    CONSTRAINT PK_INGREDIENTES_0 PRIMARY KEY (ITEM, NOME),
    CONSTRAINT FK_INGREDIENTES_0 FOREIGN KEY (ITEM)
        REFERENCES ITEM (NOME)
        ON DELETE CASCADE
);

CREATE TABLE FORNECEDOR (
    CNPJ CHAR(18) NOT NULL,
    NOME VARCHAR(32) NOT NULL,
    CONSTRAINT PK_FORNECEDOR_0 PRIMARY KEY (CNPJ),
    CONSTRAINT CK_FORNECEDOR_0 CHECK(
        CNPJ ~ '^[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}$')
);

CREATE TABLE PRODUTO (
    NOME VARCHAR(32) NOT NULL,
    CONSTRAINT PK_PRODUTO_0 PRIMARY KEY (NOME)
);

CREATE TABLE FORNECIMENTO (
    FORNECEDOR CHAR(18) NOT NULL,
    PRODUTO VARCHAR(32) NOT NULL,
    DATA DATE NOT NULL,
    QUANTIDADE INTEGER NOT NULL,
    VALOR REAL NOT NULL,
    NOTAFISCAL VARCHAR(32),
    CONSTRAINT PK_FORNECIMENTO_0 PRIMARY KEY (FORNECEDOR, PRODUTO, DATA),
    CONSTRAINT FK_FORNECIMENTO_0 FOREIGN KEY (FORNECEDOR)
        REFERENCES FORNECEDOR (CNPJ)
        ON DELETE CASCADE,
    CONSTRAINT FK_FORNECIMENTO_1 FOREIGN KEY (PRODUTO)
        REFERENCES PRODUTO (NOME)
        ON DELETE CASCADE,
    CONSTRAINT CK_FORNECIMENTO_0 CHECK(
        QUANTIDADE >= 0),
    CONSTRAINT CK_FORNECIMENTO_1 CHECK(
        VALOR >= 0)
);

CREATE TABLE ITEM_FORNECIMENTO (
    FORNECEDOR CHAR(18) NOT NULL,
    PRODUTO VARCHAR(32) NOT NULL,
    DATA DATE NOT NULL,
    ITEM VARCHAR(32) NOT NULL,
    CONSTRAINT PK_ITEM_FORNECIMENTO_0 PRIMARY KEY (FORNECEDOR, PRODUTO, DATA, ITEM),
    CONSTRAINT FK_ITEM_FORNECIMENTO_0 FOREIGN KEY (FORNECEDOR, PRODUTO, DATA)
        REFERENCES FORNECIMENTO (FORNECEDOR, PRODUTO, DATA)
        ON DELETE CASCADE,
    CONSTRAINT FK_ITEM_FORNECIMENTO_1 FOREIGN KEY (ITEM)
        REFERENCES ITEM (NOME)
        ON DELETE CASCADE
);