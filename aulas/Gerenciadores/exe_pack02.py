import tkinter as tk

class Tela:
    def __init__(self,master):
        self.janela =  master
        self.janela.geometry('400x400')

        lbl =tk.Label(self.janela, text='LEFT',bg='red').pack(ipadx=10,padx=20,side=tk.LEFT,fill= tk.Y)

        lbl1 =tk.Label(self.janela, text='RIGHT',bg='blue').pack(ipadx=10,padx=20,side=tk.RIGHT,fill=tk.X,expand=True)

        lbl2 =tk.Label(self.janela, text='LEFT2',bg='pink').pack(ipadx=10,padx=20,side=tk.LEFT,fill=tk.BOTH, expand=True)

        lbl3 =tk.Label(self.janela, text='RIGHT2',bg='black',fg='white').pack(ipadx=10,padx=20,side=tk.RIGHT,)
master = tk.Tk()
app = Tela(master)
master.mainloop()