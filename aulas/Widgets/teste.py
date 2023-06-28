import threading
import time
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry('300x200')
janela.title('Progressbar')
pause = False
def iniciar():

    #prb.start(10)
    a = p.get()
    btn_start.config(state='disabled')
    btn_pause.config(state='active')
    btn_stop.config(state='active')
    for i in range(a,101):
        if pause:
            break
        p.set(i)
        lbl['text'] = f"{prb['value']}%"
        time.sleep(0.10)

def thread():
    global pause
    pause = False
    th = threading.Thread(target=iniciar)
    th.start()

def pausar():
    global pause
    pause = True
    btn_start.config(state='active',text='Restart')

def parar():
    p.set(0)
    pausar()
    lbl.config(text= '0%')
    btn_start.config(state='active',text='Start')
    btn_pause.config(state='disabled')




p = tk.IntVar()
p.set(0)
prb = ttk.Progressbar(janela, variable=p, orient='horizontal', mode='determinate')
prb.pack()

btn_start = ttk.Button(janela, text='Start', command=thread)
btn_start.pack()

btn_pause = ttk.Button(janela, text='Pausar', command=pausar,state=tk.DISABLED)
btn_pause.pack()

btn_stop = ttk.Button(janela, text='Stop', command=parar,state=tk.DISABLED)
btn_stop.pack()

lbl = tk.Label(janela, text='')
lbl.pack()

janela.mainloop()
