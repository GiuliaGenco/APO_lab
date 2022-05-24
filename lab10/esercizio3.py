# Sviluppare la classe SortableCouple, rappresentante una coppia di valori floating point (a, b).
# Il costruttore accetta come parametri i due valori della coppia. Questi sono anche ottenibili,
# ma NON settabili, tramite properties.
# La classe implementa il metodo __repr__(self) -> str e il metodo __lt__(self, other) -> bool.
# Il secondo confronta le coppie secondo la somma dei valori a e b. Scrivere un main che crei una lista di
# SortableCouple e la riordini tramite il metodo sort.


class SortableCouple:
    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    @property
    def get_a(self):
        return self._a

    @property
    def get_b(self):
        return self._b

    def __repr__(self) -> str:
        return str(self._a) + " " + str(self._b)

    def __lt__(self, other) -> bool:
        somma1 = self._a + self._b
        somma2 = other._a + other._b
        if somma1 < somma2:
            return True
        else:
            return False


# Scrivere una classe CoupleSorter che contenga unicamente il metodo __call__(self, elm: SortableCouple) -> float che,
# ricevuto come parametro una SortableCouple, restituisca la differenza a - b.
class CoupleSorter:
    def __call__(self, elm: SortableCouple) -> float:
        return elm.get_a - elm.get_b
# Nel main, creare un'istanza di questa classe e passarla come parametro key del metodo sort che riordina la lista.
# Similmente a prima, il metodo sort userà __call__(self, elm: SortableCouple) -> float sulle SortableCouple per
# ottenere il valore con cui confrontarle. Verificare il nuovo ordinamento.


def main():
    s1 = SortableCouple(3.14, 12.5)
    s2 = SortableCouple(0, 0.5)
    s3 = SortableCouple(5.19, 10.2)
    lista = [s1, s2, s3]
    lista.sort(key=lambda s: s._a * s._b)
    # Successivamente passare come parametro key del metodo sort una funzione lambda che, preso come parametro una
    # SortableCouple, restituisca il prodotto a*b. Questa specifica un altro metodo di confronto delle SortableCouple,
    # usando come valore di confronto il prodotto dei valori contenuti. Verificare il nuovo ordinamento.
 #   print(lista)
 #  print()
    lista2 = [s2, s1, s3]
    lista2.sort(key=CoupleSorter())
    #print(lista2)


main()
