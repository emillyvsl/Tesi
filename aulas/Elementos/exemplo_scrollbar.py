import tkinter as tk
from tkinter.scrolledtext import ScrolledText
class Tela:
    def __init__(self,root):
        self.janela = root
        self.janela.title('Exemplo Text com Scrollbar')
        self.janela.geometry('400x400')
        #self.janela.resizable( width=False,height=True)
        #barra de rolagem



        scb_barra = tk.Scrollbar(self.janela)
        scb_barra.pack(side=tk.RIGHT,fill=tk.Y)

        # caixa de texto

        txt =  tk.Text(self.janela,yscrollcommand = scb_barra.set )
        txt.pack(side=tk.LEFT,fill=tk.BOTH)
        scb_barra.config(command=txt.yview)

        #cauxa de texto com barra automatica

        txt_auto = ScrolledText(self.janela)
        txt_auto.pack(side=tk.BOTTOM)

        #plaice + grid
        #






app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()