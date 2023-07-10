import tkinter as tk
from tkinter.scrolledtext import ScrolledText
janela = tk.Tk()
btn = tk.Button(janela,text='Precione qualquer tecla').pack()
scrText = ScrolledText(janela, width=50,height=10).pack()
def texto(e):
    lbl.config(text=f'apertou o botao:')

lbl = tk.Label(janela,text='').pack()
janela.bind('<KeyPress>',texto)


janela.mainloop()