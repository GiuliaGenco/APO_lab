# Creare la classe Room rappresentate una generica stanza di un'abitazione.
# I costruttore accetta come parametri il numero di metri quadri, il numero di finestre e
# il numero di prese per la corrente. Fornire un getter per ciascuna di queste proprietà.
# Creare la classe BathRoom che eredita da Room. Il costruttore, oltre ai parametri del padre,
# accetta il numero di lavandini e tre valori booleani indicanti la presenza della doccia, della vasca e del bidet.
# Scrivere dei getter per questi parametri aggiuntivi.
# Scrivere un main che crei delle istanze di queste classi. Verificare che la classe figlio possieda i
# getter del padre senza averli dovuti riscrivere.


class Room:
    def __init__(self, m2, nfinestre, nprese):
        self.m2 = m2
        self.nfinestre = nfinestre
        self.nprese = nprese

    def get_m2(self):
        return self.m2

    def get_nfinestre(self):
        return self.nfinestre

    def get_nprese(self):
        return self.nprese


class BathRoom(Room):
    def __init__(self, m2, nfinestre, nprese, nlavandini, doccia: bool, vasca: bool, bidet: bool):
        super().__init__(m2, nfinestre, nprese)  # IMPORTANTE PER EREDITARE E NON SOVRASCRIVERE
        self.nlavandini = nlavandini
        self.doccia = doccia
        self.vasca = vasca
        self.bidet = bidet

# NOTA: NON serve scrivere queste cose a meno che non voglia riscrivere i metodi: allora devo chiamarli in un'altra
#    funzione (con def) e poi modificare il mio metodo originale. In questo caso eredito direttamente dal genitore.
#     super().get_m2()
#     super().get_nfinestre()
#     super().get_nprese()
#

    def get_nlavandini(self):
        return self.nlavandini

    def con_doccia(self):
        if self.doccia is True:
            return True
        else:
            return False

    def con_vasca(self):
        if self.vasca is True:
            return True
        else:
            return False

    def con_bidet(self):
        if self.bidet is True:
            return True
        else:
            return False


def main():
    b = BathRoom(20, 1, 2, 2, True, False, True)
    print("Metri quadri ", b.get_m2())
    print("Numero di prese ", b.get_nprese())
    print("Numero di finestre ", b.get_nfinestre())
    print("Numero di lavandini ", b.get_nlavandini())
    print("C'è la vasca? ", b.con_vasca())
    print("C'è il bidet? ", b.con_bidet())
    print("C'è la doccia? ", b.con_doccia())


main()
