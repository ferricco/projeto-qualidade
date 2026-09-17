import sqlite3

conexao = sqlite3.connect("qualidade.db")

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nao_conformidades(
        id TEXT PRIMARY KEY,
        data_abertura TEXT,
        setor TEXT,
        tipo TEXT,
        descricao TEXT,
        responsavel TEXT,
        prazo TEXT,
        status TEXT,
        data_encerramento TEXT
        )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS reclamacoes_clientes(
        id TEXT PRIMARY KEY,
        data_abertura TEXT,
        cliente TEXT,
        tipo TEXT,
        descricao TEXT,
        responsavel TEXT,
        status TEXT,
        data_encerramento TEXT,
        satisfacao TEXT
        )
    """)

conexao.commit()
print("Tabela criada com sucesso!")
