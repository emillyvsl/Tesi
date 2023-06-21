import tkinter as tk
class Tela:
    def mostrar(self):
        lbl =  tk.Label(self.janela,text= self.v.get()).pack()
    def __init__(self,root):
        self.janela = root
        self.janela.title('Exemplo')
        self.janela.geometry('400x400')
        self.v = tk.StringVar()
        self.v.set('lp1')
        lbl = tk.Label(self.janela,text='Escolha uma disciplina:').pack()
        rbt_lp1 = tk.Radiobutton(self.janela,text='LP1',value= 'lp1',variable= self.v,command=self.mostrar).pack()
        rbt_tesi = tk.Radiobutton(self.janela,text='TESI',value='Tesi',variable= self.v,command=self.mostrar).pack()
        rbt_bd = tk.Radiobutton(self.janela,text='BD',value='BD',variable= self.v,command=self.mostrar).pack()



app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()