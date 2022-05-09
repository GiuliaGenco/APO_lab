# Creare un'interfaccia grafica contenente una label e un bottone.
# Ogni volta che il bottone è premuto la label deve cambiare proprio colore di sfondo.
# Scegliere a piacere quali e quanti colori utilizzare.
# Una volta passati tutti i colori di sfondo, ricominciare dal primo.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Cambia colore")

testo = StringVar()
testo.set("Nessun colore")

premuto = 0

label = ttk.Label(root, textvariable=testo)
label.config(background="white")
label.pack()


def cambiaColore():
    global premuto, testo, label
    if premuto == 0:
        label.config(background="blue")
        testo.set("blu")
        premuto += 1
    elif premuto == 1:
        label.config(background="yellow")
        testo.set("giallo")
        premuto += 1
    elif premuto == 2:
        label.config(background="green")
        testo.set("verde")
        premuto += 1
    elif premuto == 3:
        label.config(background="purple")
        testo.set("viola")
        premuto = 0


ttk.Button(root, text="Cambia colore", command=cambiaColore).pack()

root.mainloop()
