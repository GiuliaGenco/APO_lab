# problema principale: come leggo il file?
# intanto devo aprire l'input con open

fin = open("D:\POLITO\II anno\Algoritmi e Programmazione ad oggetti\Git\APO_lab\lab2\data\schieramento.txt", "r")

# per vedere se si legge il file, posso provare: print(fin.read())

# leggo il file, lo salvo e lo chiudo
tutto = fin.read()
fin.close()

# come salvo i dati senza conoscere la dimensione? posso usare una tabella
# con la tabella è più facile capire la direzione, ma una lista di stringhe era uguale (anzi meglio)

tabella = tutto.split()

# ATTENZIONE! la split però genera sempre una tabella di elementi e poi devo fare attenzione ad accedere
# perché una tabella da una riga è sempre accessibile con [0][0]:
# in questo caso la split comunque non separa gli elementi perché sono tutti attaccati tra loro

# per contare la larghezza dello schieramento basta contare il numero di "1" presente nel file e per farlo è più facile
# avere un'unica stringa con tutto il file e fare count(1)

larghezza = tutto.count("1")
print("larghezza:", larghezza)

# da cosa capiamo in numero di file? il numero più grande presente all'interno del file

nfile = max(tutto)
print("numero di file:", nfile)

# in alternativa avrei dovuto fare: nfile = max(tutto.replace("/n", "")) perché visto che sto leggendo i caratteri non
# posso essere sicura del fatto che i numeri sono maggiori dei numeri

# per trovare l'orientamento invece è possibile guardare la posizione degli 1 rispetto ai 2
# faccio due cicli while annidati per scorrere la tabella e cerco il 2

i = 0
trovato = False
while i < len(tabella) and not trovato:
    j = 0
    while j < len(tabella[0]) and not trovato:
        if tabella[i][j] == "2":
            trovato = True
        else:
            j += 1
    if not trovato:
        i += 1

# dopo aver capito la posizione del primo 2 che ho trovato cerco l'1 attorno

if i > 0 and tabella[i-1][j] == "1":
    print("direzione: Nord")
elif i < len(tabella)-1 and tabella[i+1][j] == "1":
    print("direzione: Sud")
elif j > 0 and tabella[i][j-1] == "1":
    print("direzione: Ovest")
else:
    print("direzione: Est")

# Per sapere il numero di buchi invece devo contare quanti numeri ci sono di ogni cifra.
# Quello minore avrà il maggior numero di buchi. Volendo posso saltare gli 1 perché il primo schieramento è la lunghezza

minimo = larghezza
fila = 1
for i in range(2, int(nfile)+1):
    if minimo > tutto.count(str(i)):
        minimo = tutto.count(str(i))
        fila = i

if fila == 1:
    print("Nessun buco trovato")
else:
    print("Maggior numero di buchi in fila", fila)
