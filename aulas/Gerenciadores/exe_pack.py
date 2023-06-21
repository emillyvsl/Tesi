import tkinter as tk

class Tela:
    def __init__(self,master):
        self.janela =  master
        self.janela.geometry('400x400')

        lbl =tk.Label(self.janela, text='LEFT',bg='red').pack(ipadx=10,padx=20,side=tk.LEFT,)

        lbl1 =tk.Label(self.janela, text='RIGHT',bg='blue').pack(ipadx=10,padx=20,side=tk.RIGHT,)

        lbl2 =tk.Label(self.janela, text='LEFT2',bg='red').pack(ipadx=10,padx=20,side=tk.LEFT,)

        lbl3 =tk.Label(self.janela, text='RIGHT2',bg='blue').pack(ipadx=10,padx=20,side=tk.RIGHT,)
master = tk.Tk()
app = Tela(master)
master.mainloop()