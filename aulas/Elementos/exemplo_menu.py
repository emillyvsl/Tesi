
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master): #customizar a janela
        self.janela = master
        self.janela.title('Exemplo Text com Scrollbar')
        self.janela.geometry('400x400')
        #self.janela.maxsize(400)
        #self.janela.resizable(width=True,height=True)
        #Menu
        #Menu
        mnu_barra = tk.Menu(self.janela)
        mnu_arquivo = tk.Menu(mnu_barra, tearoff=0)
        mnu_barra.add_cascade(label='Arquivo', menu=mnu_arquivo)
        mnu_arquivo.add_command(label='Novo Arquivo...')
        mnu_arquivo.add_command(label='Sair', command=self.janela.destroy)
        self.janela.config(menu=mnu_barra)

        menu_editar = tk.Menu(mnu_barra,tearoff=0)
        mnu_barra.add_cascade(label="Editar" ,menu=menu_editar)
        menu_editar.add_command(label='Copiar')
        menu_editar.add_separator()
        menu_editar.add_command(label='Colar')

        menu_pesquisar = tk.Menu(menu_editar,tearoff=0)
        menu_editar.add_cascade(label='Pesquisar',menu=menu_pesquisar)
        menu_pesquisar.add_command(label='arquivos')
        menu_pesquisar.add_command(label='texto')
        menu_pesquisar.add_command(label='animais')

        self.janela.config(menu=mnu_barra)




app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()