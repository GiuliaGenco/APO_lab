# Creare la classe Ticket rappresentate un biglietto per una coda.
# Il costruttore accetta come parametri il nome del possessore e il numero. Il metodo get_queue_pos(self)
# restituisce la posizione in coda, pari al numero del biglietto. Il metodo __repr__(self) restituisce una stringa
# contenente il nome e il numero del biglietto.
# Implementare il metodo __lt__(self, other) per confrontare i biglietti per posizione in coda.
# USARE il metodo get_queue_pos(self) per ottenere la posizione.


class Ticket:
    def __init__(self, name, num):
        self._name = name
        self._num = num

    def get_queue_pos(self):
        return self._num

    def get_name(self):
        return self._name

    def __repr__(self):
        name = self.get_name()
        num = self.get_queue_pos()
        return str(name) + " " + str(num)

    def __lt__(self, other):
        p1 = int(self.get_queue_pos())
        p2 = int(other.get_queue_pos())
        if p1 < p2:
            return p1
        else:
            return p2


# Creare la classe PriorityTicket che eredita da Ticket, per rappresentare i biglietti prioritari.
# Il costruttore accetta gli stessi parametri della classe padre, più un numero intero che indica la priorità
# Il metodo __repr__(self) restituisce una stringa contente le stesse informazioni del metodo di cui fa l'override
# (usare il metodo padre per evitare la duplicazione di codice), più il valore della priorità.
# Fare l'override di get_queue_pos(self), restituendo come posizione in coda il numero del biglietto meno la priorità
# moltiplicata per 10.

class PriorityTicket(Ticket):
    def __init__(self, name, num, priority):
        super().__init__(name, num)
        self._priority = priority

    def __repr__(self):
        s = super().__repr__()
        return s + " " + str(self._priority)

    def get_queue_pos(self):
        p = int(self._num)
        return p


# Nel main creare una lista contenete diversi biglietti, prioritari e non, e ordinarla tramite il metodo sort().
# Notare come avendo fornito un'implementazione di __lt__(self) sia possibile riordinare i biglietti per posizione.
# Notare anche come l'override di get_queue_pos(self), usato da __lt__(self, other), abbia permesso di confrontare
# biglietti delle due diverse tipologie, tenendo conto della priorità.

def fun(e):
    return e.get_queue_pos()


def main():
    b1 = Ticket("Mario Rossi", 28)
    b2 = Ticket("Giulia Genco", 36)
    b3 = PriorityTicket("Paolo Sieni Miceli", 25, 1)
    b4 = PriorityTicket("Valentina Marrazzo", 30, 2)
    lista = [b1, b2, b3, b4]
    lista.sort(key=fun)
    print(lista)


main()
