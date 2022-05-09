# Modificare l'interfaccia grafica sviluppata al punto precedente per permettere all'utente di selezionare
# direttamente il colore di sfondo da una selezione messa disposizione dal programmatore.
import tkinter as tk
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Cambia colore")
root.minsize(500, 300)

testo = StringVar()
testo.set("Nessun colore")

OptionList = ["blue", "yellow", "green", "purple"]

premuto = 0

label = ttk.Label(root, textvariable=testo, font=60, anchor=CENTER)
label.config(background="white")
label.grid(column=0, row=0)

variable = tk.StringVar(root)
variable.set(OptionList[0])


def cambiaColore(*args):  # SENZA ARGS NON FUNZIONA IL COLLEGAMENTO
    global variable, testo, premuto
    v = variable.get()
    if v == "blue":
        label.config(background="blue")
        testo.set("blu")
        print("Hai selezionato il blu")
    elif v == "yellow":
        label.config(background="yellow")
        testo.set("giallo")
        print("Hai selezionato il giallo")
    elif v == "green":
        label.config(background="green")
        testo.set("verde")
        print("Hai selezionato il verde")
    elif v == "purple":
        label.config(background="purple")
        testo.set("viola")
        print("Hai selezionato il viola")


opt = tk.OptionMenu(root, variable, *OptionList)
opt.config(width=50, font=('Helvetica', 12))
opt.grid(column=0, row=1)
variable.trace("w", cambiaColore)

# fa sì che celle della griglia si ingrandiscano
label.columnconfigure(0, weight=1)
label.rowconfigure(0, weight=1)


root.mainloop()
