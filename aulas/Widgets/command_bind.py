import  tkinter as tk
janela = tk.Tk()
def clicou():
    lbl = tk.Label(janela , text='Clicou').pack()

btn = tk.Button(janela,text='Botao',command=clicou).pack()

janela.mainloop()
