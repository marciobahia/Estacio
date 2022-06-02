from tkinter import *

window = Tk()


def botaoClicado():
    lbl.configure(text="O Botão foi Clicado")


window.title("Teste")
lbl = Label(window, text="Testando Márcio", font=("Arial", 50))
window.geometry('350x220')
botao = Button(window, text="Clique aqui", command=botaoClicado)
lbl.grid(columm=0, row=1)
window.mainloop()
