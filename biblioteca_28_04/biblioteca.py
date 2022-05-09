from scaffale import Scaffale
from libro import Libro
from utente import Utente


class Biblioteca:

    def __init__(self):
        self._libri = {}  # Devo conoscere l'elenco dei libri che contiene, ma altri non devono accedere (_)
        self._scaffali = {}  # Devo poter rintracciare uno scaffale tramite tuple scaffale-sala
        self._utenti = {}

    def add_libro(self, titolo, autore, scaffale, sala):
        # Un metodo che permette di aggiungere libri specificando titolo (stringa), autore (stringa), scaffale
        # (intero), sala (intero). Le coppie titolo autore sono univoche. Le sale sono univoche.
        # Gli scaffali sono univoci per sala.
        # NOTA: NON HO un metodo che crea lo scaffale mai: devo verificare se esiste altrimenti lo aggiungo
        if (scaffale, sala) not in self._scaffali:
            self._scaffali[(scaffale, sala)] = Scaffale(scaffale, sala)
        self._libri[(titolo, autore)] = Libro(titolo, autore, self._scaffali[(scaffale, sala)])
        self._scaffali[(scaffale, sala)].add_libro(self._libri[(titolo, autore)])

    def get_collocazione(self, titolo, autore):
        return self._libri[(titolo, autore)].get_collocazione()

    def get_libri_scaffale(self, scaffale, sala):
        return self._scaffali[(scaffale, sala)].get_libri()

    def add_utente(self, nome, codice):
        self._utenti[codice] = Utente(nome, codice)

    def prestito(self, codice, titolo, autore):
        if not self._libri[(titolo, autore)].is_in_prestito() and self._utenti[codice].get_numero_prestiti() < 6:
            self._libri[(titolo, autore)].set_utente(self._utenti[codice])
            self._utenti[codice].add_libro(self._libri[(titolo, autore)])

    def restituisci(self, titolo, autore):
        if self._libri[(titolo, autore)].is_in_prestito():
            self._libri[(titolo, autore)].restituisci()

    def get_libri_utente(self, codice):
        return self._utenti[codice].get_libri()

