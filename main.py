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