# Creare un'interfaccia grafica che gestisca un contatore circolare e visualizzi il valore attuale,
# limitato all'intervallo [0, 100]. L'utente deve poter incrementare e decrementare il valore con step 1, 2, 4 e 8.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Contatore circolare")
root.minsize(100, 200)

frame = ttk.Frame(root, borderwidth=10)
frame.grid(column=0, row=0, sticky=(N, S, W, E))

counter = IntVar()
counter.set(0)


def tastoMenoUno():
    global counter
    valattuale = int(counter.get())
    if (valattuale-1) >= 0:
        counter.set(valattuale - 1)
    else:
        counter.set(valattuale + 100)


def tastoMenoDue():
    global counter
    valattuale = int(counter.get())
    if (valattuale-2) >= 0:
        counter.set(valattuale - 2)
    else:
        counter.set(valattuale + 99)


def tastoMenoQuattro():
    global counter
    valattuale = int(counter.get())
    if (valattuale-4) >= 0:
        counter.set(valattuale - 4)
    else:
        counter.set(valattuale + 97)


def tastoMenoOtto():
    global counter
    valattuale = int(counter.get())
    if (valattuale-8) >= 0:
        counter.set(valattuale - 8)
    else:
        counter.set(valattuale + 93)


def tastoPiuUno():
    global counter
    valattuale = int(counter.get())
    if (valattuale+1) <= 100:
        counter.set(valattuale + 1)
    else:
        counter.set(valattuale - 100)


def tastoPiuDue():
    global counter
    valattuale = int(counter.get())
    if (valattuale+2) <= 100:
        counter.set(valattuale + 2)
    else:
        counter.set(valattuale - 99)


def tastoPiuQuattro():
    global counter
    valattuale = int(counter.get())
    if (valattuale+4) <= 100:
        counter.set(valattuale + 4)
    else:
        counter.set(valattuale - 97)


def tastoPiuOtto():
    global counter
    valattuale = int(counter.get())
    if (valattuale+8) <= 100:
        counter.set(valattuale + 8)
    else:
        counter.set(valattuale - 93)


label = ttk.Label(frame, textvariable=counter, font=45)
label.grid(column=0, row=0)
ttk.Button(frame, text="-1", command=tastoMenoUno).grid(column=0, row=1, sticky=W, columnspan=1)
ttk.Button(frame, text="-2", command=tastoMenoDue).grid(column=1, row=1, sticky=W, columnspan=1)
ttk.Button(frame, text="-4", command=tastoMenoQuattro).grid(column=2, row=1, sticky=W, columnspan=1)
ttk.Button(frame, text="-8", command=tastoMenoOtto).grid(column=3, row=1, sticky=W, columnspan=1)
ttk.Button(frame, text="+1", command=tastoPiuUno).grid(column=0, row=2, sticky=W, columnspan=1)
ttk.Button(frame, text="+2", command=tastoPiuDue).grid(column=1, row=2, sticky=W, columnspan=1)
ttk.Button(frame, text="+4", command=tastoPiuQuattro).grid(column=2, row=2, sticky=W, columnspan=1)
ttk.Button(frame, text="+8", command=tastoPiuOtto).grid(column=3, row=2, sticky=W, columnspan=1)


root.mainloop()
