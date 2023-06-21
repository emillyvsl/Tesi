import tkinter as tk

class Tela():
    def mostrar(self):

            lbl_texto = tk.Label(self.janela,text="Qual tipo de conteudo?").pack()
            cbt_conteudo = tk.Radiobutton(self.janela,text='Informatica',value='info').pack()
            cbt_conteudo2 = tk.Radiobutton(self.janela,text='Suporte',value='supo').pack()
            cbt_conteudo = tk.Radiobutton(self.janela,text='Programação',value='prog').pack()



    def __init__(self,master):
        self.janela = master
        self.janela.geometry('400x200')
        self.janela.title('Cadastro')
        self.aceito = tk.IntVar()

        lbl = tk.Label(self.janela,text='Você aceita receber conteudo no seu email?').pack()

        cbt_email = tk.Checkbutton(self.janela, text='Aceito receber email',variable=self.aceito,command= self.mostrar).pack()












janela = tk.Tk()
tela = Tela(janela)

janela.mainloop()
