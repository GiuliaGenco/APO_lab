# Esercizio 1
# Scrivere una classe che tenga il conto dei canestri fatti da una squadra di basket.
# Tramite il metodo add_match deve essere possibile registrare una partita, dato il nome della
# squadra avversaria e il numeri di canestri fatti.
# Il metodo get_average deve restituire la media di canestri fatti per partita.
# Il metodo get_teams deve restituire una lista contente
# i nomi delle squadre contro cui si ha giocato.
# Il metodo get_summary deve restituire una stringa che riporti il numero totale di canestri e
# la media di canestri fatti per partita.
# Scrivere una funzione main che testi le funzionalità della classe sviluppata
import statistics


class Canestri:
    def __init__(self):
        self.partiteRegistrate = {}
        self.canestri = []
        self.avversari = []

    def add_match(self, nome, numcanestri):
        self.partiteRegistrate[nome] = int(numcanestri)
        self.canestri.append(int(numcanestri))
        self.avversari.append(nome)

    def get_average(self):
        media = statistics.mean(self.canestri)
        # print("Media di canestri", media)
        return media

    def get_teams(self):
        teams = self.avversari
        print("Lista di avversari: ", teams)
        return teams

    def get_summary(self):
        canestritot = sum(self.canestri)
        print("Numero tot dei canestri: ", canestritot)
        media = self.get_average()
        print("Media dei canestri per partita: ", media)
        return canestritot, media


def Main():
    canestri = Canestri()
    canestri.add_match("Karasuno", 8)
    canestri.add_match("Nekoma", 6)
    canestri.add_match("Ebi", 4)
    canestri.get_average()
    canestri.get_teams()
    canestri.get_summary()


Main()
