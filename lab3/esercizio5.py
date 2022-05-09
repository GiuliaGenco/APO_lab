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

player = StringVar()
points = StringVar()

board = StringVar()


def inserisciGiocatore():
    global player, points, board
    dizionariogiocatori[player.get().strip()] = float(points.get())
    elenco_punteggi = [(points, player) for player, points in dizionariogiocatori.items()]
    elenco_punteggi.sort(reverse=True)

    leaderboard_box.delete(0, leaderboard_box.size() - 1)
    for pl, po in elenco_punteggi[:3]:
        leaderboard_box.insert(END, "{}: {}".format(pl, po))


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
# listbox con classifica giocatori
leaderboard_box = Listbox(root, listvariable=board, height=3)
leaderboard_box.grid(column=0, row=3, columnspan=3, sticky=(N, S, W, E))


root.mainloop()
