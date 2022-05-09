from university.corsi import Corso


class Studente:
    def __init__(self, matricola, nome, cognome):
        self._matricola = matricola
        self._nome = nome
        self._cognome = cognome
        self.corsi = {}

    def get_matricola(self):
        return self._matricola

    def get_nome(self):
        return self._nome

    def get_cognome(self):
        return self._cognome

    def add_corso(self, codice, titolo, docente):
        self.corsi[codice] = Corso(codice, titolo, docente)

    def get_corsi(self):
        return self.corsi
