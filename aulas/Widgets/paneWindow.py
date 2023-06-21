import  tkinter as tk


janela = tk.Tk()

pnw_1 = tk.PanedWindow(janela,bd=3,bg='blue',orient=tk.HORIZONTAL,width=400,height=500)
lbl_1 = tk.Label(pnw_1,text='LABEL 1')

pnw_2 = tk.PanedWindow(pnw_1,bd=3,bg='red',orient=tk.VERTICAL,showhandle=True,handlepad=15,handlesize=20)
lbl_2 = tk.Label(pnw_2,text='LABEL 2')
lbl_3 = tk.Label(pnw_2,text='LABEL 3')

pnw_1.add(lbl_1)
pnw_1.add(pnw_2)
pnw_2.add(lbl_2)
pnw_2.add(lbl_3)

pnw_1.pack()


janela.mainloop()