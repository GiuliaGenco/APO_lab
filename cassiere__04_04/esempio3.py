# Terzo esempio della cassa = qui vengono usati i metodi speciali all'interno delle classi
# in particolare tolgo la stampa

class Cassa:
    def __init__(self):
        self.aperto = False
        self.prezzi = PriceList()
        self.scontrini = []

    def nuovo_prodotto(self, code, price, name):
        self.prezzi.new_product(code, price, name)

    def apri_scontrino(self):
        if self.aperto is True:
            self.chiudi_scontrino()
        self.aperto = True
        self.scontrini.append(Receipt())

    def chiudi_scontrino(self):
        if self.aperto is True:
            self.aperto = False
            print(self.scontrini[-1])

    def scansiona_prodotto(self, code):
        if self.aperto is True:
            self.scontrini[-1].add(self.prezzi.find(code))


class Receipt:
    def __init__(self):
        self.carello = []

    def add(self, prodotto):
        self.carello.append(prodotto)

    def __repr__(self):
        # vogliamo creare un'unica stringa con tutto e non fare stampe man mano
        # quindi creo una stringa vuota e man mano concateno
        ris = ""
        tot = 0
        for p in self.carello:
            tot += p.getPrice()
            ris += str(p) + '\n'
        ris += "-" * 14 + '\n' + str(len(self.carello)) + " prodotti inseriti\nTotale " + str(tot) + "€"
        return ris


class PriceList:
    def __init__(self):
        self.elenco = {}

    def new_product(self, code, price, name):
        self.elenco[code] = Product(price, name)

    def find(self, code):
        return self.elenco[code]


class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def getPrice(self):
        return self.price

    def __repr__(self):
        # vogliamo restituire una stringa -> la f string è usabile ovunque
        return f"{self.name}  {self.price}€"


cassa = Cassa()
cassa.nuovo_prodotto(12, 1.5, "mele")
cassa.nuovo_prodotto(14, 2.5, "pere")
cassa.nuovo_prodotto(17, 3.75, "arance")

cassa.apri_scontrino()
cassa.scansiona_prodotto(12)
cassa.scansiona_prodotto(14)
cassa.scansiona_prodotto(12)
cassa.chiudi_scontrino()
