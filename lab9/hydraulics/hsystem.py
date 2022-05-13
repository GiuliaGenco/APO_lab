from hydraulics.elements import Element
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
        pass


