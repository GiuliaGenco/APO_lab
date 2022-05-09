# Creare un'interfaccia grafica che permetta d'inserire nomi di giocatori e i rispettivi punteggi (floating point).
# L'interfaccia deve aggiornare e visualizzare, in modo ordinato, nomi e punteggi dei tre miglior giocatori.
# Se un giocatore viene inserito più volte esso non deve essere duplicato,
# ma il suo ponteggio deve essere aggiornato all'ultimo fornito.

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Punteggi giocatori")
root.minsize(500, 300)

# Un dizionario funziona così
dizionariogiocatori = {}
# g1 = {"nome": "Giovanni", "punti": 21}
# dizionariogiocatori[1] = g1
# g2 = {"nome": "Giulia", "punti": 41}
# dizionariogiocatori[2] = g2
# print(dizionariogiocatori[2]["nome"])

primo = StringVar()


numG = 0

player = StringVar()
elencogiocatori = []
points = StringVar()
trovato = False


def inserisciGiocatore():
    global numG, dizionariogiocatori, points, trovato, player, elencogiocatori
    # print("Inserito:" + player.get() + points.get())
    posizione = 0
    if numG == 0:  # SE sono all'inizio
        dizionariogiocatori[numG] = {"nome": player, "punti": points}
        elencogiocatori.append(player.get())
        print("Nome inserito: " + player.get())
        print("Punteggio inserito: " + points.get())
        numG += 1
    else:

        print("Sono presenti altri giocatori. Valore di numG: ", numG)

        for p in range(len(elencogiocatori)):
            if elencogiocatori[p] == player.get():
                posizione = p
                trovato = True
            #  print("DIZIONARIO ATTUALE " + dizionariogiocatori[p]['nome'].get())

        if trovato is True:  # Se c'è già lo aggiorno
            dizionariogiocatori[posizione]['punti'] = points
            print("ATTENZIONE! Aggiorno punteggio di: " + elencogiocatori[posizione])
            print(dizionariogiocatori[posizione]['punti'].get())
            trovato = False

        else:  # Se non c'è lo aggiungo
            dizionariogiocatori[numG] = {"nome": player, "punti": points}
            elencogiocatori.append(player)
            print("Nome inserito: " + dizionariogiocatori[numG]['nome'].get())
            print("Punteggio inserito: " + dizionariogiocatori[numG]['punti'].get())
            numG += 1


# inserire un giocatore
ttk.Label(root, text="Inserire nome del giocatore:", font=45).grid(column=0, row=0, sticky=(N, S, W, E))
player_entry = Entry(root, textvariable=player)
player_entry.grid(column=1, row=0, sticky=(N, S, W, E))

ttk.Label(root, text="Inserire punti del giocatore:", font=45).grid(column=0, row=2, sticky=(N, S, W, E))
points_entry = Entry(root, textvariable=points)
points_entry.grid(column=1, row=2, sticky=(N, S, W, E))

bott1 = ttk.Button(root, text="Inserisci", command=inserisciGiocatore)
bott1.grid(column=2, row=0)

punteggi = []

for g in dizionariogiocatori:
    punteggi.append(int(dizionariogiocatori[g]['punti']))
    print("Punteggi ", punteggi[g])


# Visualizzare posti
ttk.Label(root, text="Primo posto:", font=45).grid(column=0, row=3, sticky=(N, S, W, E))
primoposto = Listbox(root, listvariable=primo, font=45)
primoposto.grid(column=1, row=3, sticky=(N, S, W, E))

root.mainloop()
