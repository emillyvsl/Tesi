import tkinter as tk
from tkinter import ttk

janela = tk.Tk()

colunas = ('nome', 'telefone', 'email')

tvw = ttk.Treeview(janela, columns=colunas, show='headings')
tvw.grid(row=0, column=0, sticky='nsew')

# Cria uma Scrollbar vertical
scrollbar = ttk.Scrollbar(janela, orient='vertical', command=tvw.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# Configura a Scrollbar para rolar a Treeview
tvw.configure(yscrollcommand=scrollbar.set)

# Cabeçalho
tvw.heading('nome', text='Nome')
tvw.heading('telefone', text='Telefone')
tvw.heading('email', text='Email')

# Colunas
tvw.column('nome', minwidth=200)

# Inserção de dados
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Em345illy', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emil34534ly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emil45t345ly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emrt35illy', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emil4t43ly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])

# Configuração de redimensionamento da janela
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

btn_editar = tk.Button(janela, text='Editar')
btn_editar.grid(row=1,column=0,rowspan=4)
btn_excluir = tk.Button(janela, text='Excluir')
btn_excluir.grid(row=1,column=1,rowspan=4)
btn_incluir = tk.Button(janela, text='Incluir')
btn_incluir.grid(row=1,column=2,rowspan=4)
btn_pesq = tk.Button(janela, text='Pesquisar')
btn_pesq.grid(row=1,column=3,rowspan=4)
janela.mainloop()
