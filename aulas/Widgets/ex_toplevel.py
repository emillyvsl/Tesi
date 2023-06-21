import tkinter as tk

class Tela():
    def __init__(self, master):

        self.janela = master
        self.janela.geometry('400x400')
        self.janela.title('Primeira Janela')

        btn = tk.Button(self.janela, text='Nova janela', command= self.nova_janela).pack()


    def nova_janela(self):
        self.toplevel = tk.Toplevel()
        self.toplevel.geometry('200x200')
        self.toplevel.title('Top level')
        #self.janela.iconify()#minimiza a janela
        #self.janela.withdraw()#oculta a janela principal, mas ela não esta parada

        self.toplevel.grab_set()#fixa a janela que esta sendo referenciada e não permite mexer em outras janelas

        btn2 = tk.Button(self.toplevel,text='Voltar', command=self.voltar).pack()

    def voltar(self):
        self.toplevel.destroy()
        self.janela.deiconify()#


app = tk.Tk()
master = Tela(app)

app.mainloop()