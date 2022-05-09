# Secondo esempio della cassa = classi in U3
# slide U2-UML pag 64: modo alternativo

class Cassa:
    def __init__(self):
        self.aperto = False
        self.prezzi = PriceList()
        self.scontrini = []

    def nuovo_prodotto(self, code, price, name):
        self.prezzi.new_product(code, price, name)

    def apri_scontrino(self):
        # se lo scontrino è aperto lo chiudiamo e viceversa
        if self.aperto is True:
            self.chiudi_scontrino()
        self.aperto = True
        self.scontrini.append(Receipt())

    def chiudi_scontrino(self):
        if self.aperto is True:
            self.aperto = False
            self.scontrini[-1].stampa()  # -1 perché voglio l'ultimo scontrino elaborato

    def scansiona_prodotto(self, code):
        if self.aperto is True:
            self.scontrini[-1].add(self.prezzi.find(code))


class Receipt:
    # ora non ha più il prezzo
    def __init__(self):
        self.carello = []

    def add(self, prodotto):
        self.carello.append(prodotto)

    def stampa(self):
        tot = 0
        for p in self.carello:
            tot += p.getPrice()
            p.stampa()
        print("-" * 14)
        print(len(self.carello), "prodotti inseriti")
        print("Totale", tot, "€")


class PriceList:
    def __init__(self):
        self.elenco = {}

    def new_product(self, code, price, name):
        self.elenco[code] = Product(price, name)
        # ATTENZIONE! in questo modo Product non conosce il suo codice ma è PriceList che abbina le due cose

    def find(self, code):
        return self.elenco[code]


class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def getPrice(self):
        return self.price

    def stampa(self):
        print(f"{self.name}  {self.price}€")


# Il client interagisce solo con la cassa questa volta:
cassa = Cassa()
cassa.nuovo_prodotto(12, 1.5, "mele")
cassa.nuovo_prodotto(14, 2.5, "pere")
cassa.nuovo_prodotto(17, 3.75, "arance")

cassa.apri_scontrino()
cassa.scansiona_prodotto(12)
cassa.scansiona_prodotto(14)
cassa.scansiona_prodotto(12)
cassa.chiudi_scontrino()
