import tkinter as tk

class Tela:
    def __init__(self,master):
        self.janela =  master

        self.janela.geometry('400x400')

        lbl =tk.Label(self.janela, text='X=0 , Y=0',bg='red').place(x=0,y=0)

        lbl2 = tk.Label(self.janela, text='x=100 , y=25',bg='pink').place(relx=.5,rely=.5,anchor=tk.CENTER)

        lbl3 = tk.Label(self.janela, text='x=200 , y=50',bg='blue').place(x=200,y=50)

        lbl4 = tk.Label(self.janela, text='x=300 , y=75',bg='pink').place(x=300,y=75)


master = tk.Tk()
app = Tela(master)
master.mainloop()