# Sviluppare la classe WeightedSorter per definire un nuovo ordinamento delle SortableCouple.
# Il costruttore accetta come parametro un valore floating point compreso nel'intervallo [0, 1],
# rappresentante il peso (weight). Esso è ottenibile e settabile tramite property.
from esercizio3 import SortableCouple


class WeightedSorter:
    def __init__(self, peso: float):
        self._valore = peso

    @property
    def valore(self):
        return self._valore

    @valore.setter
    def valore(self, nuovo_valore):
        if 0 >= nuovo_valore >= 1:
            self._valore = nuovo_valore
        else:
            raise ValueError

    def __call__(self, elm: SortableCouple) -> float:
        # Il metodo __call__(self, elm: SortableCouple) -> float, restituisce un valore di confronto della
        # SortableCouple definito come segue:
        # a * weight + b * (1 - weight)
        a = elm.get_a
        b = elm.get_b
        weight = self._valore
        return a * weight + b * (1 - weight)


def main():
    # Nel main creare una lista di SortableCouple e un'istanza della classe WeightedSorter da passare come parametro
    # key del metodo sort della lista. Come si può notare è possibile personalizzare il tipo di ordinamento creando
    # istanze apposite della classe WeightedSorter.
    s1 = SortableCouple(3.16, 1.5)
    s2 = SortableCouple(0, 0.5)
    s3 = SortableCouple(5.19, 10.2)
    lista = [s1, s2, s3]
    peso = WeightedSorter(2)
    lista.sort(key=peso)
    print(lista)


main()

# Definire una closure factory (funzione di secondo ordine) che, preso il peso weight come parametro, restituisca una
# seconda funzione (closure). La funzione restituita accetta una SortedCouple come parametro e restituisce lo stesso
# valore di confronto definito precedentemente, tramite l'utilizzo del peso weight. Equivalentemente al caso
# precedente è possibile personalizzare il tipo di ordinamento fornendo valori diversi di weight alla closure factory.
#
# Verificare che in entrambi i casi si ottiene il medesimo ordinamento della lista.


def Closure(weight):
    def function(elm: SortableCouple):
        a = elm.get_a
        b = elm.get_b
        return a * weight + b * (1 - weight)
    return function


def main2():
    s_1 = SortableCouple(3.16, 1.5)
    s_2 = SortableCouple(0, 0.5)
    s_3 = SortableCouple(5.19, 10.2)
    lista2 = [s_1, s_2, s_3]
    peso = Closure(2)
    lista2.sort(key=peso)
    print(lista2)


main2()
