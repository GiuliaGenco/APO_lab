# NOTA: ogni automa deve avere un modo diverso di muoversi: è comodo avere classi diverse che ereditano da una
from abc import ABC, abstractmethod
from random import randint


class Piano:
    def __init__(self, righe=100, colonne=100):
        self._righe = righe
        self._colonne = colonne
        self._posizioni_occupate = set()
        self._automi = []

    def is_libera(self, riga, colonna):
        if 0 <= riga < self._righe and 0 <= colonna < self._colonne and (riga, colonna) not in self._posizioni_occupate:
            return True
        else:
            return False

    def nuova_pos(self):
        r = randint(0, self._righe - 1)
        c = randint(0, self._colonne - 1)
        while not self.is_libera(r, c):
            r = randint(0, self._righe - 1)
            c = randint(0, self._colonne - 1)
        return r, c

    def alfiere(self):
        riga, colonna = self.nuova_pos()
        # NOTA: avrei anche potuto inserire tutto dentro self._automi.append(Alfiere(*self.nuova_pos())
        # L'asterisco infatti serve a spacchettare la tupla
        self._automi.append(Alfiere(riga, colonna, self))
        self._posizioni_occupate.add((riga, colonna))

    def torre(self):
        riga, colonna = self.nuova_pos()
        self._automi.append(Torre(riga, colonna, self))
        self._posizioni_occupate.add((riga, colonna))

    def pedone(self):
        riga, colonna = self.nuova_pos()
        self._automi.append(Pedone(riga, colonna, self))
        self._posizioni_occupate.add((riga, colonna))

    def muovi(self):
        for a in self._automi:
            a.muovi()

    def libera(self, pos):
        self._posizioni_occupate.remove(pos)

    def occupa(self, pos):
        self._posizioni_occupate.add(pos)

    def __repr__(self):
        ris = ""
        for a in self._automi:
            ris += str(a) + "\n"
        return ris


class Automa(ABC):
    def __init__(self, r, c, p):
        self._riga = r
        self._colonna = c
        self._piano = p

    def muovi(self):
        nuova_pos = self.posizione_futura()
        if self._piano.is_libera(*nuova_pos):
            self._piano.libera((self._riga, self._colonna))  # ATTENZIONE: IMPORTANTI LE DOPPIE PARENTESI X TUPLA
            self._piano.occupa(nuova_pos)
            self._riga = nuova_pos[0]
            self._colonna = nuova_pos[1]

    def __repr__(self):
        return f'{type(self).__name__} {self._riga} {self._colonna}'

    @abstractmethod
    def posizione_futura(self):
        pass


class Alfiere(Automa):
    # Nota: funziona anche senza costruttore perché viene recuperato nel padre

    def posizione_futura(self):
        direzione = randint(0, 3)  # Scelgo N,S,E,W -> nota che Randint prende anche l'ultimo valore incluso
        spostamento = randint(1, 10)
        if direzione == 0:
            ris = (self._riga + spostamento, self._colonna + spostamento)
        elif direzione == 1:
            ris = (self._riga + spostamento, self._colonna - spostamento)
        elif direzione == 2:
            ris = (self._riga - spostamento, self._colonna - spostamento)
        else:
            ris = (self._riga - spostamento, self._colonna + spostamento)
        return ris


class Torre(Automa):
    # Le torri si muovono in modo rettilineo in una direzione casuale con uno spostamento fra 1 e 10 caselle
    def posizione_futura(self):
        direzione = randint(0, 3)  # Scelgo N,S,E,W -> nota che Randint prende anche l'ultimo valore incluso
        spostamento = randint(1, 10)
        if direzione == 0:
            ris = (self._riga + spostamento, self._colonna)
        elif direzione == 1:
            ris = (self._riga, self._colonna - spostamento)
        elif direzione == 2:
            ris = (self._riga - spostamento, self._colonna)
        else:
            ris = (self._riga, self._colonna + spostamento)
        return ris


class Pedone(Automa):
    # I pedoni si muovono in modo rettilineo in una direzione casuale con uno spostamento di una casella.
    def posizione_futura(self):
        direzione = randint(0, 3)
        if direzione == 0:
            ris = (self._riga + 1, self._colonna)
        elif direzione == 1:
            ris = (self._riga, self._colonna - 1)
        elif direzione == 2:
            ris = (self._riga - 1, self._colonna)
        else:
            ris = (self._riga, self._colonna + 1)
        return ris
