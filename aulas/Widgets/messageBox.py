import tkinter as tk
from tkinter import messagebox


def aviso():
    messagebox.showinfo('Aviso',"Você clicou no botão")
def erro():
    messagebox.showerror('Erro','Torcer pelo Flamengo')
def pergunta():
    messagebox.askyesno('Pergunta','Confirma que a shayraraca é feio?')
    if (resposta == True:
        messagebox.showinfo('Ok','Ok')
    else:
        messagebox.showwarning('Voltar','Voltar')
janela = tk.Tk()


btn1 = tk.Button(janela,text='Aviso', command=aviso).pack()

btn2 = tk.Button(janela,text='Erro',command=erro).pack()

btn3 = tk.Button(janela,text='Pergunta',command=pergunta).pack()


janela.mainloop()