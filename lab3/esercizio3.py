# Creare un'interfaccia grafica che permetta di visualizzare
# il contenuto del file sabato.txt, mantenendo gli a capo quando presenti.
# L'intero testo non deve essere visibile contemporaneamente, ma deve essere accessibile
# tramite una barra di scorrimento verticale posta a lato.

from tkinter import *
from tkinter import ttk

FILE = 'D:\POLITO\II anno\Algoritmi e Programmazione ad oggetti\Git\APO_lab\lab3\data\sabato.txt'

file = open(FILE, 'r')
# Salvo in una lista ogni frase del testo separatamente per mantenere gli a capo
testo = []

for line in file:
    testo.append(line.strip())

file.close()

# crea finestra principale e frame
root = Tk()
root.title("Lettore testo")
root.minsize(500, 200)

frame = ttk.Frame(root, borderwidth=5, relief="ridge")
frame.grid(column=0, row=0, sticky=(N, S, W, E))

# configura griglia del frame e di root per ridimensionare righe e colonne se finestra viene ingrandita
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text_box = Text(frame)
text_box.grid(column=0, row=0, sticky=(N, S, W, E))
for line in testo:
    text_box.insert(END, line + "\n")  # SENZA END NON FUNZIONA

scroll_bar = ttk.Scrollbar(frame, orient=VERTICAL, command=text_box.yview)
scroll_bar.grid(column=1, row=0, sticky=(N, S, W, E))

# a sua volta la textbox, quando viene "scrollata",
# chiama un callback (metodo set della scrollbar) che sposta la barra di scorrimento
text_box['yscrollcommand'] = scroll_bar.set


root.mainloop()
