# Esercizio 1
# Scrivete un programma che legga una parola da console e visualizzi tutte le sue sottostringhe,
# ordinate per lunghezza crescente.
# Se, ad esempio, l’utente fornisce la stringa *“rum”*, il programma deve visualizzare:
# ```
# r
# u
# m
# ru
# um
# ```

parola = input("Inserire la parola:  ")
conto = 0

for lettera in parola:
    print(lettera)
    conto += 1

# print(range(conto))
# controllo che non ci sia meno di due lettere e faccio un ciclo al contrario per evitare errore del contatore (range)
if conto > 1:
    for lett in range(conto):
        if lett > 0:
            print(parola[lett - 1] + parola[lett])

# bisogna capire come fare le altre sottostringhe
