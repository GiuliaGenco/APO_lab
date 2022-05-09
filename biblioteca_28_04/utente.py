# L'utente deve per forza sapere quali libri in prestito ha per poter restituire poi la lista

class Utente:
    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = codice
        self._libri = set()

    def get_numero_prestiti(self):
        return len(self._libri)

    def add_libro(self, libro):
        self._libri.add(libro)

    def restituisci(self, libro):
        self._libri.remove(libro)

    def get_libri(self):
        ris = []
        for l in self._libri:
            ris.append(l.get_dati())
        return ris
