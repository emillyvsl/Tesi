import tkinter as tk # Importando a biblioteca tk

class Tela:
    def mostar(self):
        lbl_mostar= tk.Label(self.janela)
        lbl_mostar['text'] = self.basico.get()

        lbl_mostar.pack()


    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('400x200') # Dimensão da janela 400x200
        self.janela.title('Exemplo CheckButton')
        self.basico = tk.IntVar()#variavel inteira
        self.avancado = tk.IntVar()

        cbt_basico = tk.Checkbutton(self.janela,
                                    text='Basico',
                                    variable=self.basico,command=self.mostar).pack()
        cbt_avancado = tk.Checkbutton(self.janela,
                                      text='Avançado',
                                      variable=self.avancado).pack()








janela = tk.Tk() # Criando uma janela tkinter
tela = Tela(janela)
# Laço infinito para iniciar e manter a aplicação
janela.mainloop()