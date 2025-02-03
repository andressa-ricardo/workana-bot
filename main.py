import tkinter as tk
from tkinter import messagebox
from src.bot.workana_bot import executar_bot  

def iniciar_automacao():
    email = email_entry.get()
    senha = senha_entry.get()

    if not email or not senha:
        messagebox.showwarning("Dados Faltando", "Insira seu email e senha")
        return

    try:
        executar_bot(email, senha)
        messagebox.showinfo("Sucesso", "Automação concluída com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a execução: {e}")

janela = tk.Tk()
janela.title("Bot workana")
janela.geometry("400x200")

email_label = tk.Label(janela, text="Email:")
email_label.pack(pady=10)

email_entry = tk.Entry(janela, width=30)
email_entry.pack()

senha_label = tk.Label(janela, text="Senha:")
senha_label.pack(pady=10)

senha_entry = tk.Entry(janela, show="*", width=30)
senha_entry.pack()

iniciar_button = tk.Button(janela, text="Iniciar Automação", command=iniciar_automacao)
iniciar_button.pack(pady=20)

janela.mainloop()
