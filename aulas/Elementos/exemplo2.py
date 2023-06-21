import tkinter as tk #importando necessario

class Tela:
    def __init__(self,master):
        self.janela=master
        self.janela.title('Primeira janela')#definindo o titulo da janela
        self.janela.geometry('500x500')#tamanho da janela largura e altura,usar somente esse pq o usuario é burro
        #janela.minsize(200,400)#tamanho minimo da janela
        #janela.maxsize(800,600)#tamanho maximo
        self.janela.resizable(width=False,height=False)#não deixar o usuario redimensionar
        #conteiner
        conteiner1 = tk.Frame(self.janela,borderwidth=5,bg='red',width=100,height=100,relief=tk.RAISED)#como parametro deve ter o construtor acima dele, o costrutor pai
        conteiner1.pack()
        conteiner2 = tk.Frame(self.janela,borderwidth=5,bg='blue',width=100,height=100,relief=tk.SUNKEN)#como parametro deve ter o construtor acima dele, o costrutor pai
        conteiner2.pack()

janela = tk.Tk()#necessario para iniciar a interface
tela = Tela(janela)
janela.mainloop()#obrigatoirio estar no fim

