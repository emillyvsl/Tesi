import tkinter as tk #importando necessario

janela = tk.Tk()#necessario para iniciar a interface
janela.title('Primeira janela')#definindo o titulo da janela
janela.geometry('500x500')#tamanho da janela largura e altura,usar somente esse pq o usuario é burro
#janela.minsize(200,400)#tamanho minimo da janela
#janela.maxsize(800,600)#tamanho maximo
janela.resizable(width=False,height=False)#não deixar o usuario redimensionar

conteiner1 = tk.Frame(janela,borderwidth=5,bg='red',width=100,height=100,relief=tk.RAISED)#como parametro deve ter o construtor acima dele, o costrutor pai
conteiner1.pack()
conteiner2 = tk.Frame(janela,borderwidth=5,bg='blue',width=100,height=100,relief=tk.SUNKEN)#como parametro deve ter o construtor acima dele, o costrutor pai
conteiner2.pack()
janela.mainloop()#obrigatoirio estar no fim
#essas tres coisas são obrigatorias para iniciar uma interface
