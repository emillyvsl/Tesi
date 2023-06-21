import tkinter as tk

janela = tk.Tk()

imagem = tk.PhotoImage(file='logo.png')

lbl = tk.Label(janela,image= imagem).pack()



janela.mainloop()