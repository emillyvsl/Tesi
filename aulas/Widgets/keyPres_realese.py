import  tkinter as tk
janela = tk.Tk()
janela.geometry('400x400')
def keypres(evento):
    lbl.config(text='precionou')
def release(evento):
    lbl.config(text='Soltou')

lbl = tk.Label(janela , text='Gsqw')
lbl.pack()
janela.bind('KeyPress',keypres)
janela.bind('KeyRelease',release,add='+')


janela.mainloop()
