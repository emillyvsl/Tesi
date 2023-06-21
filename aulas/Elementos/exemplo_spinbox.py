
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:


    def mostra(self):
        lbl_mostra = tk.Label(self.janela,text=self.v.get())
        lbl_mostra.pack()
    def __init__(self, master): #customizar a janela
        self.janela = master
        self.janela.title('Exemplo Text com Scrollbar')
        self.janela.geometry('400x400')
        self.v = tk.StringVar()
        spb_mes = tk.Spinbox(self.janela,from_=1, to=12,wrap=True,command=self.mostra)
        spb_mes.pack()

        scl_volume = tk.Scale(self.janela,from_=0 , to=100,orient=tk.VERTICAL, variable=self.v,command=self.mostra).pack()

        scl_volu = tk.Scale(self.janela,from_=0 , to=100,orient=tk.HORIZONTAL).pack()


app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()