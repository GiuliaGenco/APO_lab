class Libro:
    def __init__(self, titolo, autore, scaffale):
        self.titolo = titolo
        self.autore = autore
        self.scaffale = scaffale  # NOTA: Scaffale è un oggetto ricollegato alla sua classe
        self._utente = None  # Mi serve sapere chi ha il libro in questo momento e da qui capisco se è in prestito

    def get_collocazione(self):
        return self.scaffale.get_collocazione()

    def get_dati(self):
        return (self.titolo, self.autore)

    def set_utente(self, utente):
        self._utente = utente

    def is_in_prestito(self):
        if self._utente is None:
            return False
        else:
            return True

    def restituisci(self):
        self._utente.restituisci(self)
        self._utente = None
