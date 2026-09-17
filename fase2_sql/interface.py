import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Sistema de Qualidade")
janela.geometry("500x600")

titulo = ctk.CTkLabel(janela, text="Cadastro de Não Conformidade",
                      font=ctk.CTkFont(size=16, weight="bold"))

titulo.pack(pady=20)

campo_id = ctk.CTkEntry(janela, placeholder_text="ID (ex: NC-0062)", width=300)
campo_id.pack(pady=5)

campo_data = ctk.CTkEntry(janela, placeholder_text="Data de abertura (DD/MM/AAAA)", width=300)
campo_data.pack(pady=5)

campo_setor = ctk.CTkOptionMenu(janela, values=["Produção", "Laboratório", "Expedição", "Almoxarifado", "Manutenção"], width=300)
campo_setor.pack(pady=5)

campo_tipo = ctk.CTkEntry(janela, placeholder_text="Tipo de NC", width=300)
campo_tipo.pack(pady=5)

campo_descricao = ctk.CTkEntry(janela, placeholder_text="Descrição da NC", width=300)
campo_descricao.pack(pady=5)

campo_responsavel = ctk.CTkEntry(janela, placeholder_text="Responsável pela NC", width=300)
campo_responsavel.pack(pady=5)

campo_prazo = ctk.CTkEntry(janela, placeholder_text="Prazo", width=300)
campo_prazo.pack(pady=5)

campo_status = ctk.CTkOptionMenu(janela, values=["Aberta", "Em análise", "Em tratamento", "Encerrada"], width=300)
campo_status.pack(pady=5)

def salvar_nc():
    conexao = sqlite3.connect("qualidade.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO nao_conformidades
        (id, data_abertura, setor, tipo, descricao, responsavel, prazo, status, data_encerramento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            campo_id.get(),
            campo_data.get(),
            campo_setor.get(),
            campo_tipo.get(),
            campo_descricao.get(),
            campo_responsavel.get(),
            campo_prazo.get(),
            campo_status.get(),
            None
    ))

    conexao.commit()
    conexao.close()

    campo_id.delete(0, "end"),
    campo_data.delete(0, "end"),
    campo_setor.set("Produção"),
    campo_tipo.delete(0, "end"),
    campo_descricao.delete(0, "end"),
    campo_responsavel.delete(0, "end"),
    campo_prazo.delete(0, "end"),
    campo_status.set("Aberta")

    mensagem.configure(text="Registro salvo com sucesso!")

mensagem = ctk.CTkLabel(janela, text="")
mensagem.pack(pady=5)

botao = ctk.CTkButton(janela, text="Salvar", command=salvar_nc, width=300)
botao.pack(pady=20)

janela.mainloop()