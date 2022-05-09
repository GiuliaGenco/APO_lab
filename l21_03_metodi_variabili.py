# METODI APPLICABILI

frase = "Ciao, come stai oggi?    "
a = frase

# in questo modo a diventa una freccia verso frase, ma ad a posso applicare anche dei metodi con il punto

a = frase.strip()  # strip toglie gli spazi e gli a capo alla fine
print(a)

# ma a catena posso eseguire un altro metodo
a = frase.strip().upper()  # prima viene eseguito strip e poi upper
print(a)

# posso anche creare una lista con la split ed eseguire i metodi delle liste
a = frase.strip().upper().split()
print(a)

# per usare i metodi delle liste devo selezionare com le quadre l'elemento all'interno della lista
a = frase.strip().split()[0].upper()
print(a)

# oppure posso usare i metodi delle funzioni
a = frase.strip().split().sort()
print(a)  # in questo caso compare 'none' come risultato perché sort ordina la lista su cui è stato eseguito
# e il risultato non è un dato! Il metodo sort non restituisce niente
# qui sort non ha effetto su niente perché la ordina ma non la restituisce.
# Va eseguito su lista che ha già riferimento perché altrimenti non lo salva

# anche metodi come 'append' restituiscono il none
a = frase.strip().split().append("Bene grazie!")
print(a)

# bisogna quindi fare molta attenzione ad usare i metodi


# LE FUNZIONI E LE VARIABILI LOCALI E GLOBALI
B = 10  # NON è nè in una classe nè in una funzione quindi è visibile ovunque ed è GLOBALE
c = [3]  # se c è una lista nella funzione posso usare i suoi metodi! L'importante è che c
# rimanga la freccia verso il contenuto in memoria: NON POSSO STRAVOLGERE IL RIFERIMENTO


def f():
    a = 12
    c.append(2)
#  B = 15 questa B è una NUOVA VARIABILE LOCALE con lo stesso nome ma separata (e infatti mi dà errore)

# la variabile a è interna alla funzione ed è quindi LOCALE
# non posso fare assegnazioni di variabili globali in una funzione! posso usarla solo nella funzione
print(c)