# Sviluppare la classe astratta Shape che eredita da ABC, rappresentante una figura geometrica. Il costruttore accetta
# come unico parametro il nome che si vuole associare alla figura. (ad es., "figura1", "la mia forma", etc...)
# Il nome deve essere ottenibile tramite opportuno getter. La classe possiede due metodi astratti che restituiscono,
# rispettivamente, il perimetro e l'area della figura.
#
# La classe Square eredita da Shape e rappresenta un quadrato. Il suo costruttore, oltre a nome del quadrato, accetta
# la lunghezza del lato. Implementare i metodi astratti della classe padre che restituiscono l'area e il perimetro.
import math
from abc import ABC


class Shape(ABC):
    def __init__(self, nome: str):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def get_perimetro(self):
        pass

    def get_area(self):
        pass


class Triangle(Shape):
    def __init__(self, nome: str, lbase: int, l1=0, l2=0):
        super().__init__(nome)
        self._lbase = lbase
        self._l1 = l1
        self._l2 = l2

    def get_perimetro(self):
        # La classe Triangle, rappresentante un triangolo, eredita da Shape. Il suo costruttore, oltre al nome
        # del triangolo, accetta la lunghezza della base e un numero variabile di lunghezze degli altri lati.
        # Se viene fornita solo la lunghezza della base il triangolo è equilatero, se viene fornita la lunghezza
        # di un altro lato il triangolo è isoscele, altrimenti è scaleno.
        # Implementare i metodi astratti che della classe padre che restituiscono area e il perimetro.
        # Per il calcolo dell'area in modo generico si può utilizzare la formula di Erone.
        if self._l1 == 0 and self._l2 == 0:
            # Se il triangolo è equilatero
            perimetro = self._lbase * 3
        elif self._l2 == 0:
            # Se il triangolo è isoscele
            perimetro = self._l1 * 2 + self._lbase
        else:
            perimetro = self._lbase + self._l1 + self._l2
        return perimetro

    def get_area(self):
        perimetro = self.get_perimetro()/2
        a = self._lbase
        if self._l1 == 0 and self._l2 == 0:
            # Se il triangolo è equilatero
            area = math.sqrt(perimetro * (perimetro - a) ** 3)
        elif self._l2 == 0:
            # Se il triangolo è isoscele
            b = self._l1
            area = math.sqrt(perimetro * (perimetro - a) * (perimetro - b) ** 2)
        else:
            area = math.sqrt(perimetro * (perimetro - a) * (perimetro - self._l2) * (perimetro - self._l1))
        return area


class Square(Shape):
    def __init__(self, nome: str, lato: float):
        super().__init__(nome)
        self._lato = lato

    def get_perimetro(self):
        return self._lato * 4

    def get_area(self):
        return self._lato * self._lato


teq = Triangle("t1", 3)
print(teq.get_perimetro())
print(teq.get_area())

ti = Triangle("t2", 3, 2)
print(ti.get_area())
print(ti.get_perimetro())

ts = Triangle("t3", 3, 2, 4)
print(ts.get_perimetro())
print(ts.get_area())

s = Square("q1", 2)
print(s.get_area())
print(s.get_perimetro())
