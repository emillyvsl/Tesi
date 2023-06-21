import tkinter as tk # Importando a biblioteca tk

class Tela:

    def logar(self):
        lbl_teste = tk.Label(janela,text='clicou').pack()

    def __init__(self,janela):
        janela.geometry('400x200') # Dimensão da janela 400x200
        janela.title('Login')
        # Label e entry usuário
        lbl_usu = tk.Label(janela,text='Usuário:',font=('calibre',10,'bold')).pack()
        ent_usu = tk.Entry(janela, width = 20).pack()

        # Label e entry senha
        lbl_senha = tk.Label(janela, text='Senha:',font=('calibre',10,'bold')).pack()
        ent_senha = tk.Entry(janela, width = 20, show='*').pack()

        btn_logar = tk.Button(janela, text='Entrar', command=self.logar,bg='green').pack()

        btn_fechar = tk.Button(janela, text='Fechar', command=janela.destroy,bg='red').pack()

janela = tk.Tk() # Criando uma janela tkinter
tela = Tela(janela)
# Laço infinito para iniciar e manter a aplicação
janela.mainloop()