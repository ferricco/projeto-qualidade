import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Sistema de Qualidade")
janela.geometry("500x600")

titulo = ctk.CTkLabel(janela, text="Cadastro de Reclamação",
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

def salvar_nc():
    conexao = sqlite3.connect("qualidade.db")
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO reclamacoes_clientes
    (id, data_abertura, cliente, tipo, descricao, responsavel, status, data_encerramento, satisfacao)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,(
        campo_id.get(),
        campo_data_abertura.get(),
        campo_cliente.get(),
        campo_tipo.get(),
        campo_descricao.get(),
        campo_responsavel.get(),
        campo_status.get(),
        None,
        None
    ))

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

mensagem = ctk.CTkLabel(janela, text="")
mensagem.pack(pady=5)

botao = ctk.CTkButton(janela, text="Salvar", command=salvar_nc, width=300)
botao.pack(pady=20)

janela.mainloop()

