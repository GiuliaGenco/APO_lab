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
        tipo.strip().lower()
        if tipo == "source":
            elm = Source(nome)
            print("Hai aggiunto source")
        elif tipo == "tap":
            elm = Tap(nome)
            print("Hai aggiunto tap")
        elif tipo == "sink":
            elm = Sink(nome)
            print("Hai aggiunto sink")
        elif tipo == "split":
            elm = Split(nome)
            print("Hai aggiunto split")
        else:
            raise ValueError

        sistema.add_element(elm)
        messagebox.showinfo(title="Success!", message="Element added")


# gestisco finestra info
def get_student():
    messagebox.showinfo(title="Student found!", message=str(sistema.get_elements()))


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
    tipo = StringVar()
    nome = StringVar()
    tipo_entry = ttk.Entry(win, textvariable=tipo)
    nome_entry = ttk.Entry(win, textvariable=nome)
    tipo_entry.grid(column=1, row=0, sticky=(N, S, W, E))
    nome_entry.grid(column=1, row=1, sticky=(N, S, W, E))
    # creo bottone
    b = ttk.Button(win, text="Aggiungi", command=lambda: add_element(tipo.get(), nome.get()))
    b.grid(column=0, row=2, columnspan=2, sticky=(N, S, W, E))



# finestra principale
root = Tk()
root.title("Sistema Idraulico")
root.minsize(500, 300)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

b1 = ttk.Button(root, text="Add Element", command=show_add_elem_window)
b1.grid(column=0, row=0, sticky=(N, S, W, E))

elenco = sistema.get_elements()
print("Elenco in sistema: ", elenco)
lvar = StringVar(value=elenco)
fin = Listbox(root, listvariable=lvar, font=45)
fin.grid(column=0, row=1, sticky=(N, S, W, E))

root.mainloop()
