import tkinter as tk

#serve para organizar componentes

janela = tk.Tk()
janela.geometry('400x400')

frame1 = tk.Frame(janela,bg='pink',width=200)
frame1.pack(side=tk.TOP,expand=True, fill=tk.X)
btn1 = tk.Button(frame1,text='1').pack()
btn2 = tk.Button(frame1,text='2').pack()
btn3 = tk.Button(frame1,text='3').pack()

frame2 = tk.Frame(janela,bg='red',width=100)
frame2.pack(side=tk.BOTTOM,expand=True, fill=tk.X)
btn4 = tk.Button(frame2,text='4').grid(row=0,column=0)
btn5 = tk.Button(frame2,text='5').grid(row=0,column=1)
btn6 = tk.Button(frame2,text='6').grid(row=1,column=0,columnspan=2)



janela.mainloop()