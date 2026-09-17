import pandas as pd
import sqlite3

conexao = sqlite3.connect("qualidade.db")

cursor = conexao.cursor()

df_nc = pd.read_excel("base_qualidade.xlsx", sheet_name="nao_conformidades").dropna(how="all")
df_rec = pd.read_excel("base_qualidade.xlsx", sheet_name="reclamacoes_clientes").dropna(how="all")

df_nc.columns = ["id", "data_abertura", "setor", "tipo", "descricao", "responsavel", "prazo", "status", "data_encerramento"]
df_rec.columns = ["id", "data_abertura", "cliente", "tipo", "descricao", "responsavel", "status", "data_encerramento", "satisfacao"]

df_nc.to_sql("nao_conformidades", conexao, if_exists="replace", index=False)
df_rec.to_sql("reclamacoes_clientes", conexao, if_exists="replace", index=False)

cursor.execute("SELECT COUNT(*) FROM nao_conformidades")
print("Total de NCs no banco:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM reclamacoes_clientes")
print("Total de reclamações no banco:", cursor.fetchone()[0])
