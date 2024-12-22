import sqlite3 as con

# Criar tabelas
sql_cliente = '''
    CREATE TABLE IF NOT EXISTS Cliente (
    ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    RG VARCHAR (12) NOT NULL,
    Nome_Cliente VARCHAR(30) NOT NULL,
    Sobrenome_Cliente VARCHAR(40),
    Telefone VARCHAR(12),
    Rua VARCHAR(40),
    Numero VARCHAR(5),
    Bairro VARCHAR(25)
    )
'''

sql_produtos = '''
    CREATE TABLE IF NOT EXISTS Produto(
    ID_Produto INTEGER PRIMAY KEY AUTOINCREMENT,
    Nome_Produto VARCHAR (30) NOT NULL,
    Tipo_Produto VARCHAR (25) NOT NULL,
    Preco DECIMAL (10, 2) NOT NULL,
    Qtde_Estoque SMALLINT NOT NULL
    );
'''

sql_vendas = '''
    CREATE TABLE IF NOT EXISTS Venda (
    ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    Nota_Fiscal SMALLINT NOT NULL,
    ID_Cliente INTEGER NOT NULL,
    Data_Compra DATETIME,
    ID_Produto INTEGER NOT NULL,
    Quantidade SMALLINT NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREIGN KEY (ID_Produto) REFERENCES Produto(ID_Produto))
'''