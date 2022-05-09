# fare calcolatrice con la possibilità di usare delle lambda function nei button:
# non voglio farla a mano ma automatizzarla con un ciclo

from tkinter import *
from tkinter import ttk

COLONNE = 4

nomiBottoni = "123+456-789*0/%="


def schiaccia(tasto):
    global valore
    v = valore.get()
    if tasto == "=":
        # eval è una funzione che esegue una stringa come se fosse un pezzo di codice
        # NOTA: le operazioni saranno in formato python (es ** = ^ )
        try:
            valore.set(eval(v))
        except:
            valore.set("ERRORE")

    elif v == "0" or v == "ERRORE":
        valore.set(tasto)
    else:
        valore.set(v + tasto)


root = Tk()
root.title("Calcolatrice")

# creo il valore inserito nella calcolatrice
valore = StringVar()
valore.set("0")

schermo = ttk.Label(root, textvariable=valore, background="white", anchor="e", font=("", 20))
schermo.grid(row=0, column=0, columnspan=COLONNE, sticky="ewns")

# faccio un ciclo per mettere i bottoni
for i in range(len(nomiBottoni)):
    ttk.Button(root, text=nomiBottoni[i], command=lambda a=nomiBottoni[i]: schiaccia(a)).grid(row=1 + i // COLONNE,
                                                                                              column=i % COLONNE)

# possiamo intercettare i numeri schiacciati dall'utente sulla tastiera (collego la corrispondente keysyms)
for j in range(10):
    root.bind("<Key-" + str(j) + ">", lambda e, a=str(j): schiaccia(a))

# per collegare invece i simboli devo collegare sia i simboli della tastiera che quelli a cui associo il valore
# posso farlo a mano
root.bind("<Return>", lambda e: schiaccia("="))

# oppure con un dizionario
operatori = {"plus": "+", "minus": "-", "asterisk": "*", "slash": "/", "equal": "=", "Return": "="}
for k in operatori:
    root.bind("<" + k + ">", lambda e, a=operatori[k]: schiaccia(a))

root.mainloop()
