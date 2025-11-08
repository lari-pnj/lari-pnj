import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('titulo da janela')
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("550x450")

tk.Label(root, text="minha primeira janela").pack()
tk.Label(root, text="eai galeres").pack()


##image = tk.PhotoImage(file ="img1.gif") ##adiciona imagem dos arquivos
##tk.Label(root, image=image).pack()  ##adiciona a imagem a janela

widgets = [  ## Tipos de widgets 
    tk.Label, ## Apenas um rotulo, não interativo
    tk.Checkbutton, ## Uma caixa de seleção
    ttk.Combobox, ## Uma caixa de lista suspensa
    tk.Entry,  ## Insira uma liha de texto
    tk.Button, ## Adiciona um botao
    tk.Radiobutton, ## Um conjunto de alternância, com apenas um item ativo
    tk.Scale,  ## Um controle deslizante
    tk.Spinbox,  ##  	Um spinner inteiro
]

##"w", tk.W(para o Oeste) 	Alinha com a borda esquerda
##"e", tk.E(para o Leste) 	Alinha com a borda direita
##"center",tk.CENTER 	Centraliza horizontalmente no espaço disponível

##"n", tk.N(para o Norte) 	Alinha com o topo
##"s", tk.S(para o Sul) 	Alinha com a parte inferior
##"center",tk.CENTER 	Centraliza verticalmente no espaço disponível

#label = tk.Label(self, text="Hello", anchor="center")

for widget in widgets:
    try:
        widget = widget(root, text=widget.__name__)
    except tk.TclError:
        widget = widget(root)
    widget.pack(padx=5, pady=5, fill="x")
    
            
        






root.mainloop()