# esempio delle classi in U3
# slide U2-UML pag 63: costruire un sistema per gestire la cassa di un negozio

# 1 = costruisco tre classi che mi interessano: Receipt, PriceList e Product
# 2 = parto da Product, poi gestisco PriceList e poi Receipt

class Receipt:
    # dovrà avere elenco di prodotti e poi dovrà avere la priceList
    def __init__(self, prezzi):
        self.prezzi = prezzi
        # mi serve una lista con i miei prodotti nel carrello: in questo modo posso fare l'append
        self.carello = []

    def add(self, code):
        # il codice ci viene dato quando creiamo lo scontrino
        self.carello.append(self.prezzi.find(code))

    def stampa(self):
        # devo stampare: elenco, numero di prodotti e totale
        tot = 0
        for p in self.carello:
            tot += p.getPrice()
            p.stampa()
        print("-"*14)
        print(len(self.carello), "prodotti inseriti")
        print("Totale", tot)


class PriceList:
    # come sempre devo inizializzare il costruttore (in questo caso non ha attributi ma ha
    # relazioni con receipt che con product: find ha elenco dei prodotti e ne restituisce uno -> dizionario)
    def __init__(self):
        # dobbiamo creare un dizionario vuoto per poter fare delle aggiunte
        # self indica sempre l'oggetto su cui sto lavorando
        self.elenco = {}

    # ora creiamo i metodi
    # nota: in python formalmente i nomi dei metodi vengono scritti con _ in mezzo, ma in Java si usa nomeGrande
    def new_product(self, code, price, name):
        self.elenco[code] = Product(price, name)

    def find(self, code):
        return self.elenco[code]


class Product:
    # inizializzo il costruttore (self è obbligatorio, gli altri due vengono presi e usati come locali):
    def __init__(self, price, name):
        self.price = price
        self.name = name
        # Spesso in tutti i linguaggi nei costruttori: collego l'istanza al dato locale
        # self.price e price sono due cose distinte riferite a pezzi di memoria diversi: gli dò lo stesso nome
        # ma sono due cose diverse. Non è una regola ma una possibilità

    # Ora passo a costruire i metodi di Product:
    def getPrice(self):
        return self.price

    # Con le graffe inserisco la variabile da stampare
    # dopo self.name e self.price posso scrivere dopo i due punti le caratteristiche di stile che mi interessano
    # es. Allineamento, grandezza ecc.

    def stampa(self):
        print(f"{self.name}  {self.price}€")


# Per capire se tutto il codice che abbiamo scritto fino ad ora funziona abbiamo bisogno di creare un Client
# che usi le nostre classi

# Per prima cosa creiamo la lista di prodotti
pl = PriceList()
pl.new_product(12, 34.4, "pere")
pl.new_product(15, 10.2, "mele")
pl.new_product(2, 10.2, "arance")

scontrino = Receipt(pl)
scontrino.add(12)
scontrino.add(15)
scontrino.add(12)
scontrino.stampa()
