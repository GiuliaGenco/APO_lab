from hydraulics.elements import Element, Source
from typing import List


class HSystem:
    def __init__(self) -> None:
        self.elements = []  # Componenti che formano il sistema idraulico

    def add_element(self, elm: Element) -> None:
        # È possibile aggiungere elementi al sistema tramite il metodo add_element(self, elm: Element) -> None
        # di HSystem, il quale riceve come parametro un oggetto di tipo Element e lo aggiunge ai componenti che
        # formano il sistema idraulico.
        self.elements.append(elm)

    def get_elements(self) -> List[Element]:
        # Tramite il metodo get_elements(self) -> List[Element] è possibile ottenere una lista contenente
        # gli elementi presenti nel sistema.
        return self.elements

    def simulate(self) -> List[str]:
        # Idea: parto dalla sorgente, simulo la sorgente e poi pian piano ogni elemento a cui è collegato fino al sink
        # Problema: negli sdoppi ci sono tante cose da fare, quindi quando arrivo alla biforcazione devo salvare
        # il percorso che devo ancora esplorarlo: aggiungo alla lista elemento ancora da simulare nella mia lista.
        # Quando la mia lista sarà vuota allora posso finire la simulazione
        sim_list = []
        to_simulate = []
        for elm in self.elements:
            # Devo trovare la sorgente e appena trovata faccio partire la simulazione
            if isinstance(elm, Source):
                to_simulate += elm.simulate(None, sim_list)
                # print("simulazione : ", sim_list)
        while to_simulate:
            # finché la lista ha elementi li simulo
            elm, inflow = to_simulate[-1]
            to_simulate = to_simulate[:-1]  # Tolgo il primo elemento che sto simulando
            # Ora devo simulare l'elemento
            to_simulate += elm.simulate(inflow, sim_list)
            # print(elm.get_name())
        return sim_list
