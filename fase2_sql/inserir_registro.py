import sqlite3

conexao = sqlite3.connect("qualidade.db")

cursor = conexao.cursor()

print("=== Cadastro de Não Conformidade ===\n")

id = input("ID (ex: NC-0061): ")
data_abertura = input("Data de abertura (DD/MM/AAAA): ")
setor = input("Setor: ")
tipo = input("Tipo de NC: ")
descricao = input("Descrição: ")
responsavel = input("Responsável: ")
prazo = input("Prazo (DD/MM/AAA): ")
status = input("Status: ")

cursor.execute("""
    INSERT INTO nao_conformidades
    (id, data_abertura, setor, tipo, descricao, responsavel, prazo, status, data_encerramento)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id, data_abertura, setor, tipo, descricao, responsavel, prazo, status, None))

conexao.commit()
print("\nRegistro cadastrado com sucesso!")

