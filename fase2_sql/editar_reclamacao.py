import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Sistema de Qualidade")
janela.geometry("500x600")

titulo = ctk.CTkLabel(janela, text="Editar Reclamação",
                      font=ctk.CTkFont(size=16, weight="bold"))

titulo.pack(pady=0)

campo_id = ctk.CTkEntry(janela, placeholder_text="ID (ex: REC-0041)", width=300)
campo_id.pack(pady=5)

campo_data_abertura = ctk.CTkEntry(janela, placeholder_text="Data de abertura (DD/MM/AAAA)", width=300)
campo_data_abertura.pack(pady=5)

campo_cliente = ctk.CTkEntry(janela, placeholder_text="Cliente", width=300)
campo_cliente.pack(pady=5)

campo_tipo = ctk.CTkEntry(janela, placeholder_text="Tipo de reclamação", width=300)
campo_tipo.pack(pady=5)

campo_descricao = ctk.CTkEntry(janela, placeholder_text="Descrição", width=300)
campo_descricao.pack(pady=5)

campo_responsavel = ctk.CTkEntry(janela, placeholder_text="Responsável", width=300)
campo_responsavel.pack(pady=5)

campo_status = ctk.CTkOptionMenu(janela, values=["Aberta", "Em análise", "Em tratamento", "Encerrada"])
campo_status.pack(pady=5)

campo_data_encerramento = ctk.CTkEntry(janela, placeholder_text="Data de encerramento (DD/MM/AAAA)", width=300)
campo_data_encerramento.pack(pady=5)

campo_satisfacao = ctk.CTkEntry(janela, placeholder_text="Satisfação", width=300)
campo_satisfacao.pack(pady=5)


def buscar_nc():
    mensagem.configure(text="")

    if campo_id.get() == "":
        mensagem.configure(text="Digite um ID para buscar")
        return

    conexao = sqlite3.connect("qualidade.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM reclamacoes_clientes WHERE id = ?", (campo_id.get(),))

    registro = cursor.fetchone()
    if registro:
        campo_id.delete(0, "end")
        campo_id.insert(0, registro[0])
        campo_data_abertura.delete(0, "end")
        campo_data_abertura.insert(0, registro[1])
        campo_cliente.delete(0, "end")
        campo_cliente.insert(0, registro[2])
        campo_tipo.delete(0, "end")
        campo_tipo.insert(0, registro[3])
        campo_descricao.delete(0, "end")
        campo_descricao.insert(0, registro[4])
        campo_responsavel.delete(0, "end")
        campo_responsavel.insert(0, registro[5])
        campo_status.set(registro[6])
        campo_data_encerramento.delete(0, "end")
        campo_data_encerramento.insert(0, registro[7] if registro[7] else "")
        campo_satisfacao.delete(0, "end")
        campo_satisfacao.insert(0, registro[8] if registro[8] else "")
    else:
        campo_id.delete(0, "end"),
        campo_data_abertura.delete(0, "end"),
        campo_cliente.delete(0, "end"),
        campo_tipo.delete(0, "end"),
        campo_descricao.delete(0, "end"),
        campo_responsavel.delete(0, "end"),
        campo_status.set("Aberta")
        campo_data_encerramento.delete(0, "end")
        campo_satisfacao.delete(0, "end")
        mensagem.configure(text="ID não encontrado")

def editar_nc():

    if campo_id.get() == "":
        mensagem.configure(text="Digite um ID para editar")
        return

    try:
        conexao = sqlite3.connect("qualidade.db")
        cursor = conexao.cursor()

        cursor.execute("""
        UPDATE reclamacoes_clientes
        SET status = ?, data_encerramento = ?, satisfacao = ?
        WHERE id = ?
        """, (campo_status.get(), campo_data_encerramento.get(), campo_satisfacao.get(), campo_id.get()))

        conexao.commit()
        conexao.close()

        campo_id.delete(0, "end"),
        campo_data_abertura.delete(0, "end"),
        campo_cliente.delete(0, "end"),
        campo_tipo.delete(0, "end"),
        campo_descricao.delete(0, "end"),
        campo_responsavel.delete(0, "end"),
        campo_status.set("Aberta")
        campo_data_encerramento.delete(0, "end")
        campo_satisfacao.delete(0, "end")

        mensagem.configure (text="Registro salvo com sucesso!")

    except sqlite3.DatabaseError as erro:
        conexao.rollback()
        mensagem.configure(text=f"Erro no banco de dados {erro}")

    except Exception as e:
        conexao.rollback()
        mensagem.configure(text=f"Falha ao salvar no banco de dados. Erro: {e}")


mensagem = ctk.CTkLabel(janela, text="")
mensagem.pack(pady=5)

botao_buscar = ctk.CTkButton(janela, text="Buscar", command=buscar_nc, width=300)
botao_buscar.pack(pady=20)

botao_salvar = ctk.CTkButton(janela, text="Salvar", command=editar_nc, width=300)
botao_salvar.pack(pady=20)

janela.mainloop()