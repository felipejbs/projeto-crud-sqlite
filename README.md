# projeto-crud-sqlite

# 💐 Sistema de Gerenciamento de Floricultura

Este projeto consiste na criação de um banco de dados em SQLite para gerenciar **clientes**, **produtos** e **vendas** de uma floricultura.

## 📦 Estrutura do Projeto

O script Python cria automaticamente o banco de dados `floricultura.db` com as seguintes tabelas:

### 🧑 Cliente
Armazena informações básicas dos clientes da floricultura.

| Campo              | Tipo        | Descrição                        |
|--------------------|-------------|----------------------------------|
| ID_Cliente         | INTEGER     | Identificador único (PK)         |
| RG                 | VARCHAR(12) | Documento de identificação       |
| Nome_Cliente       | VARCHAR(30) | Primeiro nome                    |
| Sobrenome_Cliente  | VARCHAR(40) | Sobrenome                        |
| Telefone           | VARCHAR(12) | Número de telefone               |
| Rua                | VARCHAR(40) | Nome da rua                      |
| Numero             | VARCHAR(5)  | Número da residência             |
| Bairro             | VARCHAR(25) | Bairro                           |

### 🌺 Produto
Contém os produtos vendidos pela floricultura.

| Campo         | Tipo         | Descrição                        |
|---------------|--------------|----------------------------------|
| ID_Produto    | INTEGER      | Identificador único (PK)         |
| Nome_Produto  | VARCHAR(30)  | Nome do produto                  |
| Tipo_Produto  | VARCHAR(25)  | Tipo ou categoria do produto     |
| Preco         | DECIMAL(10,2)| Preço unitário                   |
| Qtde_Estoque  | SMALLINT     | Quantidade disponível em estoque |

### 💰 Venda
Registra as vendas realizadas.

| Campo         | Tipo        | Descrição                          |
|---------------|-------------|------------------------------------|
| ID_Transacao  | INTEGER     | Identificador único da venda (PK) |
| Nota_Fiscal   | SMALLINT    | Número da nota fiscal              |
| ID_Cliente    | INTEGER     | Cliente associado à venda (FK)     |
| Data_Compra   | DATETIME    | Data e hora da compra              |
| ID_Produto    | INTEGER     | Produto vendido (FK)               |
| Quantidade    | SMALLINT    | Quantidade vendida                 |

## 🛠 Como usar

1. Certifique-se de ter o Python instalado.
2. Execute o script com o seguinte comando:

```bash
python main.py
