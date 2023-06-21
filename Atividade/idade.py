import tkinter as tk

class Tela():
    def logar(self):
        try:
            lbl_teste = tk.Label(janela,text=f'{self.nome.get()}, sua idade atual é: {2023 - int(self.idade.get())}').pack()
        except:
            lbl =tk.Label(janela,text='Entre com um valor inteiro!!').pack()


    def __init__(self,master):
        janela = master
        janela.geometry('400x200')
        janela.title('Idade')
        self.idade = tk.IntVar()
        self.nome = tk.StringVar()

        lbl_usu = tk.Label(janela,text='Nome:',font=('calibre',10,'bold')).pack()
        ent_usu = tk.Entry(janela, width = 20,textvariable=self.nome).pack()


        lbl_senha = tk.Label(janela, text='Ano de nascimento:',font=('calibre',10,'bold')).pack()
        ent_senha = tk.Entry(janela, width = 20,textvariable= self.idade).pack()

        btn_idade = tk.Button(janela, text='Idade', command=self.logar,bg='#87CEFA').pack()






janela = tk.Tk()
tela = Tela(janela)

janela.mainloop()
