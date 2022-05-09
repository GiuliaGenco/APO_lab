class Scaffale:

    def __init__(self, scaffale, sala):
        self._scaffale = scaffale
        self._sala = sala
        self._libri = []

    def add_libro(self, libro):
        self._libri.append(libro)  # NOTA: libro è direttamente un oggetto

    def get_collocazione(self):
        return (self._scaffale, self._sala)

    def get_libri(self):
        ris = []
        for l in self._libri:
            ris.append(l.get_dati())
        return ris
