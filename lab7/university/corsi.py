from studenti import Studente


class Corso:
    def __init__(self, codice, titolo, docente):
        self._codice = codice
        self._titolo = titolo
        self._docente = docente
        self.studenti_iscritti = {}

    def get_cod(self):
        return self._codice

    def get_titolo(self):
        return self._titolo

    def get_docente(self):
        return self._docente

    def add_student(self, matricola, nome, cognome):
        self.studenti_iscritti[matricola] = Studente(matricola, nome, cognome)

    def get_students(self):
        return self.studenti_iscritti
