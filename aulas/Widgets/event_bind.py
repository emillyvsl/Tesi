import  tkinter as tk
janela = tk.Tk()
def clicou(evento):
    lbl = tk.Label(janela , text='Clicou')
    lbl.pack()
    print(evento)

btn = tk.Button(janela,text='Botao')
btn.bind('<Return>',clicou)
btn.pack()
janela.bind('keyPress')
# btn.bind('<Control-a>',clicou)#usando dois botoes para realizar um evento

janela.mainloop()
