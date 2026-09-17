import sqlite3

conexao = sqlite3.connect("qualidade.db")

cursor = conexao.cursor()

print("=== Cadastro de Reclamação de cliente ===\n")

id = input("ID (ex: REC-0041): ")
data_abertura = input("Data de abertura (DD/MM/AAAA): ")
cliente = input("Cliente: ")
tipo = input("Tipo de REC: ")
descricao = input("Descrição: ")
responsavel = input("Responsável: ")
status = input("Status: ")

cursor.execute("""
    INSERT INTO reclamacoes_clientes
    (id, data_abertura, cliente, tipo, descricao, responsavel, status, data_encerramento, satisfacao)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (id, data_abertura, cliente, tipo, descricao, responsavel, status, None, None))

conexao.commit()
print("\nRegistro cadastrado com sucesso")