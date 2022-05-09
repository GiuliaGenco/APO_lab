from tkinter import *
from tkinter import ttk

# questo va scritto sempre nei programmi per aprire una finestra:
root = Tk()
root.title("Calcolatrice")

# per far vedere l'elemento creato devo usare la grid o il .pack() alla fine che mette tutto uno sotto l'altro
l = ttk.Label(root, text="Calcolatrice", background="red").pack()

# frame è invisibile a prescindere: infatti non si vede nemmeno con il pack ma serve a creare spazi
frame = ttk.Frame().pack

valore = StringVar()
valore.set("0")
schermo = ttk.Label(root, textvariable=valore, background="yellow").pack()


# come funziona un bottone:

def tasto1():
    dato = valore.get()
    if dato == '0':
        valore.set("1")
    else:
        valore.set(dato+"1")

def tastoSomma():
    valore.set(valore.get() + "+")

def tastoUguale():
    if "+" in valore.get():
        dati= valore.get().split("+")
        a = int(dati[0])
        b = int(dati[1])
        s = a + b
        valore.set(str(s))

# attenzione! quando richiami la funzione nel bottone se non ci sono parametri non mettere le parentesi
ttk.Button(root, text="1", command=tasto1).pack()
ttk.Button(root, text="+", command=tastoSomma).pack()
ttk.Button(root, text="=", command=tastoUguale).pack()

# questo serve a mostrarci la parte grafica
root.mainloop()
