import tkinter as tk

class Tela:
    def __init__(self,master):
        self.janela =  master
        self.janela.geometry('400x400')

        lbl =tk.Label(self.janela,text='Login:').grid(row=0,column=0)
        ent = tk.Entry(self.janela).grid(row=0,column=1)

        lbl2 =tk.Label(self.janela,text='Senha:').grid(row=1,column=0)
        ent2 = tk.Entry(self.janela).grid(row=1,column=1)

        btn = tk.Button(self.janela,text='Entrar').grid(row=2, column=0,columnspan=2)


master = tk.Tk()
app = Tela(master)
master.mainloop()