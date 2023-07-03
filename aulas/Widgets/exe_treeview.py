import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

tvw = ttk.Treeview(janela)
tvw.pack()
alunos = tvw.insert('','end',text='alunos')
professores= tvw.insert('','end',text='professores')
tvw.insert(alunos,'end',text='emi')
tvw.insert(professores,'end',text='sthe')
tvw.insert(alunos,'end',text='dimi')
tvw.insert(professores,0,text='dfgdfg')



janela.mainloop()