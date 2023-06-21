import tkinter as tk
def abrir_janela():
    toplevel = tk.Toplevel()
    toplevel.title('Nova janela')
    lbl = tk.Label(toplevel,tex)

janela = tk.Tk()
janela.geometry('400x400')
janela.title('Janela principal das aplicação')

btn = tk.Button(janela,text="Nova janela", command=abrir_janela).pack()

janela.mainloop()