from typing import List, Optional
from abc import ABC
import abc


class Element(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.ingresso = None
        self.uscita = None

    def get_name(self) -> str:
        # Tutti gli elementi hanno un nome che può essere letto tramite il metodo get_name(self) -> str
        return str(self.name)

    def connect(self, elm: "Element") -> None:  # ATTENZIONE PROBLEMA: ho riscritto ma non so se funziona
        # È possibile connettere l'uscita di un elemento all'ingresso di un altro tramite il metodo
        # connect(self, elm: "Element") -> None Il metodo riceve come parametro l'elemento al cui ingresso deve
        # essere connessa l'uscita dell'elemento sui cui è invocato. Ad esempio, a.connect(b) connette
        # l'uscita di a all'ingresso di b. Il metodo, se invocato su un oggetto Sink, non ha nessun effetto.
        self.uscita = elm
        elm.set_ingresso(self)

    def get_output(self) -> Optional["Element"]:
        # Dato un elemento semplice qualunque, è possibile sapere a quale altro elemento è connessa la sua uscita,
        # tramite il metodo get_output(self) -> Optional["Element"] che restituisce un oggetto di tipo Element.
        # Se nessun elemento è collegato alla sua uscita restituisce None (il type hint Optional serve proprio a
        # indicare la possibilità di avere None come valore di ritorno).
        return self.uscita

    def get_ingresso(self):
        return self.ingresso

    def get_uscita(self):
        return self.uscita

    def set_ingresso(self, ing):
        self.ingresso = ing

    def set_uscita(self, usc):
        self.uscita = usc

    @abc.abstractmethod
    def simulate(self, inflow, sim_list):
        pass


class Source(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._flow = 0

    def set_flow(self, flow: float) -> None:
        # definire la portata per una sorgente (Source) con il metodo set_flow(self, flow: float) -> None,
        # che riceve come parametro un numero reale che rappresenta i metri cubi al secondo erogati dalla sorgente
        self._flow = flow

    def simulate(self, inflow, sim_list):
        sim_list.append("Source {} {:.3f} {:.3f}".format(self.name, 0, self._flow))
        # Per poter creare la lista di oggetti ancora da simulare li ritorno
        return [(self.uscita, self._flow)]


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._open = False
        self._portataUscita = 0
        self._portataIngresso = None

    def set_status(self, to_open: bool = True) -> None:
        self._open = to_open
        # if to_open is True:
        #     self._portataUscita = self._portataIngresso

    def set_portataIngresso(self, pi):
        self._portataIngresso = pi

    def simulate(self, inflow, sim_list):
        outflow = 0
        if self._open:
            outflow = inflow
        sim_list.append("Tap {} {:.3f} {:.3f}".format(self.name, inflow, outflow))
        return [(self.uscita, outflow)]


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def connect(self, elm: "Element") -> None:
        pass

    def simulate(self, inflow, sim_list):
        sim_list.append("Sink {} {:.3f} {:.3f}".format(self.name, inflow, 0))
        return []


class Split(Element):
    #  L'elemento a T, rappresentato dalla classe Split, permette di suddividere l'ingresso in
    #  due flussi in uscita uguali tra loro.
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.prima_uscita = None
        self.seconda_uscita = None

    def connect_at(self, elm: Element, pos: int) -> None:
        # Per tale classe il metodo connect_at(self, elm: Element, pos: int) -> None riceve un ulteriore parametro,
        # di tipo intero, che indica il numero dell'uscita a cui connettere l'elemento. Tale intero ha valore 0 per
        # la prima uscita e 1 per la seconda.
        if pos == 0:
            self.prima_uscita = elm
        elif pos == 1:
            self.seconda_uscita = elm
        else:
            raise ValueError

    def get_outputs(self) -> List[Optional[Element]]:
        # Per sapere quali elementi sono connessi in uscita a un elemento a T, è possibile utilizzare il metodo
        # get_outputs(self) -> List[Optional[Element]], che restituisce una lista con i due elementi connessi.
        # Se un'uscita non è connessa ad alcun elemento, inserire None nella lista al posto dell'elemento.
        lista = [self.prima_uscita, self.seconda_uscita]
        return lista

    def simulate(self, inflow, sim_list):
        outflow = inflow / 2
        sim_list.append("Split {} {:.3f} {:.3f} {:.3f}".format(self.name, inflow, outflow, outflow))
        return [(self.prima_uscita, outflow), (self.seconda_uscita, outflow)]
