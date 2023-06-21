import tkinter as tk

class Tela:
    def __init__(self,master):
        self.janela = master
        self.janela.title('Exemplo label')
        self.janela.geometry('300x500')
        lbl_primeira = tk.Label(self.janela,fg = 'white', # Opções do label
                                bg = '#808080',
                                width = 20,
                                height = 5,
                                #anchor = tk.S,
                                padx = 10,
                                pady = 10,
                                relief = tk.RIDGE,
                                text='Senhor me ajudaaa!',font=('calibre',10,'bold'))
        self.janela
        lbl_primeira.pack()


master = tk.Tk()
app = Tela(master)
master.mainloop()