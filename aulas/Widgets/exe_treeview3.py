import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def __init__(self,master):
        self.janela = master
        colunas = ('nome', 'telefone', 'email')
        
        self.tvw = ttk.Treeview(self.janela, columns=colunas, show='headings')
        self.tvw.grid(row=0, column=0, sticky='nsew')
        
        # Cria uma Scrollbar vertical
        scrollbar = ttk.Scrollbar(self.janela, orient='vertical', command=self.tvw.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Configura a Scrollbar para rolar a Treeview
        self.tvw.configure(yscrollcommand=scrollbar.set)
        
        # Cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('telefone', text='Telefone')
        self.tvw.heading('email', text='Email')
        
        # Colunas
        self.tvw.column('nome', minwidth=200)
        
        # Inserção de dados
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Em345illy', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emil34534ly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emil45t345ly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emrt35illy', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emil4t43ly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        self.tvw.insert('', 'end', values=['Emilly', '9999', 'emi@sou.ufac.br'])
        
        # Configuração de redimensionamento da self.janela
        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)

        frame_btn = tk.Frame(self.janela)
        frame_btn.grid(row=1,column=0)
        
        btn_editar = tk.Button(frame_btn, text='Editar',command=self.editar)
        btn_editar.grid(row=0,column=0)

        btn_excluir = tk.Button(frame_btn, text='Excluir',command=self.excluir)
        btn_excluir.grid(row=0,column=1)

        btn_incluir = tk.Button(frame_btn, text='Incluir',command=self.cadastrar)
        btn_incluir.grid(row=0,column=2)

        btn_pesq = tk.Button(frame_btn, text='Pesquisar')
        btn_pesq.grid(row=0,column=3)
    def cadastrar(self):
        self.top_cadastrar = tk.Toplevel()
        lbl_nome = tk.Label(self.top_cadastrar,text='Nome:')
        lbl_nome.grid(row=0,column=0)

        lbl_tel = tk.Label(self.top_cadastrar,text='Telefone:')
        lbl_tel.grid(row=1,column=0)

        lbl_email = tk.Label(self.top_cadastrar,text='Email:')
        lbl_email.grid(row=2,column=0)

        self.ent_nome = tk.Entry(self.top_cadastrar)
        self.ent_nome.grid(row=0,column=1)

        self.ent_tel = tk.Entry(self.top_cadastrar)
        self.ent_tel.grid(row=1,column=1)

        self.ent_email = tk.Entry(self.top_cadastrar)
        self.ent_email.grid(row=2,column=1)

        btn_confirmar = tk.Button(self.top_cadastrar, text='Confirmar',command=self.confirmar_cadastro)
        btn_confirmar.grid(row=3,column=0,columnspan=2)
    def confirmar_cadastro(self):

        nome = self.ent_nome.get()
        telefone = self.ent_tel.get()
        email = self.ent_email.get()
        if(nome == " " or email== ''or telefone == " "):
            messagebox.showinfo('Aviso','Por favor preencha todos os campos!!!',parent=self.top_cadastrar)
        else:
            self.tvw.insert('','end',values=[nome,telefone,email])
            self.top_cadastrar.destroy()
    def excluir(self):
       tupla = self.tvw.selection()
       for i in tupla:
           self.tvw.delete(i)

    def editar(self):

        item = self.tvw.selection()
        if (len(item)!=1):
            messagebox.showwarning('Aviso','SELECIONE APENAS UM ITEM')
        else:
            var = self.tvw.item(item,'values')#devolve os valores do item selecionado
            print(var)
            self.top_editar = tk.Toplevel()
            lbl_nome = tk.Label(self.top_editar,text='Nome:')
            lbl_nome.grid(row=0,column=0)

            lbl_tel = tk.Label(self.top_editar,text='Telefone:')
            lbl_tel.grid(row=1,column=0)

            lbl_email = tk.Label(self.top_editar,text='Email:')
            lbl_email.grid(row=2,column=0)

            self.ent_nome = tk.Entry(self.top_editar)
            self.ent_nome.grid(row=0,column=1)
            self.ent_nome.insert('end',var[0])

            self.ent_tel = tk.Entry(self.top_editar)
            self.ent_tel.grid(row=1,column=1)
            self.ent_tel.insert('end',var[1])

            self.ent_email = tk.Entry(self.top_editar)
            self.ent_email.grid(row=2,column=1)
            self.ent_email.insert('end',var[2])

            btn_confirmar = tk.Button(self.top_editar, text='Confirmar',command=self.confirmar_edicao)
            btn_confirmar.grid(row=3,column=0,columnspan=2)

    def confirmar_edicao(self):

        nome = self.ent_nome.get()
        telefone = self.ent_tel.get()
        email = self.ent_email.get()
        selecionado = self.tvw.selection()
        if(nome == " " or email== ''or telefone == " "):
            messagebox.showinfo('Aviso','Por favor preencha todos os campos!!!',parent=self.top_cadastrar)
        else:
            self.tvw.item(selecionado,values=[nome,telefone,email])
            self.top_editar.destroy()


janela = tk.Tk()
app=Tela(janela)
janela.mainloop()
