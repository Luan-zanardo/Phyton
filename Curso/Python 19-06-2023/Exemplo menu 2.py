import tkinter as tk
print("ola")
def exibir_mensagens_simultaneas():
    num_mensagens = 100000

    for _ in range(num_mensagens):
        janela_erro = tk.Toplevel(janela)
        janela_erro.title("Erro")
        mensagem_erro = tk.Label(janela_erro, text="Ocorreu um erro!")
        mensagem_erro.pack()

# Cria a janela principal
janela = tk.Tk()

# Botão para exibir as mensagens de erro simultaneamente
while True:
    exibir_mensagens_simultaneas()

# Inicia o loop da janela
janela.mainloop()