# versione senza canvas CON LE LABMDA FUNCION PER EVITARE RIPETIZIONI

# importo tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Gioco del Tris")

s = ttk.Style()
s.configure("new.TButton", font=("", 20))  # così posso richiamare direttamente lo stile

# creo una matrice 3x3 per le caselle del tris
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for r in range(3):
    for c in range(3):
        b[r][c] = ttk.Button(root, command=lambda a=r,b=c: p(a, b), style="new.TButton")
        b[r][c].grid(row=r, column=c, sticky="nsew")

# per gestire l'inserimento di una mossa dobbiamo sapere a che giocatore tocca e quindi il simbolo da utilizzare
simboli = ["O", "X"]
turno = 0

# dobbiamo gestire la condizione di vittoria e bloccare il gioco quando qualcuno vince
vittoria = False

# creo una matrice di stringhe vuote per riempirle poi con le mosse
matrice = [["", "", ""], ["", "", ""], ["", "", ""]]


def check(tot):
    global vittoria
    if not vittoria and 3 in tot["O"]:
        vittoria = True
        print("Ha vinto il giocatore 1: O")
    if not vittoria and 3 in tot["X"]:
        vittoria = True
        print("Ha vinto il giocatore 2: X")


def controllaVittoria():
    # devo cercare elementi uguali nella matrice
    for i in range(3):
        totali = {"O": [0, 0], "X": [0, 0], "": [0, 0]}
        # uso un dizionario per tenere i conti di quanti in riga e quanti in colonna
        for j in range(3):
            totali[matrice[i][j]][0] += 1
            totali[matrice[j][i]][1] += 1
            # Sto esaminando in contemporanea le righe e le colonne: i è quello che al momento non cambia
        check(totali)
        # ora devo verificare la diagonale
        totali = {"O": [0, 0], "X": [0, 0], "": [0, 0]}
        for j in range(3):
            totali[matrice[j][j]][0] += 1
            totali[matrice[j][2-j]][1] += 1
        check(totali)


# quando schiaccio i bottoni:

def p(r, c):
    # devo verificare se il bottone è già stato premuto e quindi se c'è qualcosa scritto nella matrice
    global turno
    if not vittoria and matrice[r][c] == "":
        matrice[r][c] = simboli[turno]
        b[r][c]["text"] = simboli[turno]
        controllaVittoria()
        turno = (turno+1) % 2


# sistemo le dimensioni dei quadrati
dim = 200

for i in range(3):
    root.columnconfigure(i, minsize=dim)
    root.rowconfigure(i, minsize=dim)


# voglio che schiacciando il + si ingrandisca e con il - si riduca
def ingrandisci():
    global dim
    dim += 10
    for i in range(3):
        root.columnconfigure(i, minsize=dim)
        root.rowconfigure(i, minsize=dim)


def riduci():
    global dim
    dim -= 10
    for i in range(3):
        root.columnconfigure(i, minsize=dim)
        root.rowconfigure(i, minsize=dim)


root.bind("<plus>", lambda e: ingrandisci())  # è importante questa forma o mettere la e nella parentesi quando def la f
root.bind("<minus>", lambda e: riduci())

root.mainloop()
