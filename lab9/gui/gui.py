# L'interfaccia deve permettere all'utente di visualizzare l'elenco di elementi presenti nel sistema,
# mostrandone tipo e nome.
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from hydraulics.elements import Source, Tap, Sink, Split
from hydraulics.hsystem import HSystem

# Sviluppare un'interfaccia grafica che, utilizzando il package hydraulics, permetta di aggiungere elementi
# al sistema idraulico specificandone il tipo e il nome.

sistema = HSystem()


def add_element(tipo, nome):
    if tipo != "" and nome != "":
        if tipo == "Source":
            elm = Source(nome)
            print("Hai aggiunto source")
        elif tipo == "Tap":
            elm = Tap(nome)
            print("Hai aggiunto tap")
        elif tipo == "Sink":
            elm = Sink(nome)
            print("Hai aggiunto sink")
        elif tipo == "Split":
            elm = Split(nome)
            print("Hai aggiunto split")
        else:
            raise ValueError

        sistema.add_element(elm)
        e.append(nome)
        print("Elementi presenti: ", e)
        messagebox.showinfo(title="Success!", message="Element added")


def show_add_elem_window():
    # creo finestra
    win = Toplevel(root)
    win.title('Add element')
    win.minsize(500, 100)
    # configuro griglia
    win.columnconfigure(0, weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=1)
    win.rowconfigure(2, weight=1)
    # creo labels
    l1 = ttk.Label(win, text="Tipo: ")
    l2 = ttk.Label(win, text="Nome: ")
    l1.grid(column=0, row=0, sticky=(N, S, W, E))
    l2.grid(column=0, row=1, sticky=(N, S, W, E))
    # creo entries
    nome = StringVar()
    OptionList = [
        "Source",
        "Tap",
        "Sink",
        "Split"
    ]
    variable = StringVar()
    variable.set(OptionList[0])
    tipo_entry = OptionMenu(win, variable, *OptionList)
    nome_entry = ttk.Entry(win, textvariable=nome)
    tipo_entry.grid(column=1, row=0, sticky=(N, S, W, E))
    nome_entry.grid(column=1, row=1, sticky=(N, S, W, E))
    # creo bottone
    b = ttk.Button(win, text="Aggiungi", command=lambda: add_element(variable.get(), nome.get()))
    b.grid(column=0, row=2, columnspan=2, sticky=(N, S, W, E))


def show_elem_window():
    win2 = Toplevel(root)
    win2.title('Show element')
    win2.minsize(500, 100)
    # configuro griglia
    win2.columnconfigure(0, weight=1)
    win2.columnconfigure(1, weight=1)
    win2.rowconfigure(0, weight=1)
    win2.rowconfigure(1, weight=1)
    win2.rowconfigure(2, weight=1)
    lvar.set(e)
    fin = Listbox(win2, listvariable=lvar, font=45)
    fin.grid(column=0, row=1, sticky=(N, S, W, E))


# finestra principale
root = Tk()
root.title("Sistema Idraulico")
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

b1 = ttk.Button(root, text="Add Element", command=show_add_elem_window)
b1.grid(column=0, row=0, sticky=(N, S, W, E))
b2 = ttk.Button(root, text="Show Elements", command=show_elem_window)
b2.grid(column=0, row=1, sticky=(N, S, W, E))

lvar = StringVar()
e = []


root.mainloop()
