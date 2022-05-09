from typing import List

from university import Studente, Corso


class University:

    # R1
    def __init__(self, name: str) -> None:
        self._nome_ateneo = name
        self._rettore = ""
        self._studenti = {}
        self._corsi = {}
        self._matr_counter = 1000
        self._cod_counter = 10

    def get_name(self) -> str:
        return self._nome_ateneo

    def set_rector(self, name: str, surname: str) -> None:
        self._rettore = str(name + " " + surname)

    def get_rector(self) -> str:
        return self._rettore

    # R2
    def add_student(self, name: str, surname: str) -> int:
        matricola = self._matr_counter
        self._studenti[matricola] = Studente(matricola, name, surname)
        self._matr_counter += 1
        return matricola

    def get_student_info(self, student_id: int) -> str:
        nome = self._studenti[student_id].get_nome()
        cognome = self._studenti[student_id].get_cognome()
        return str(student_id) + " " + nome + " " + cognome

    # R3
    def add_course(self, title: str, teacher: str) -> int:
        codice = self._cod_counter
        self._corsi[codice] = Corso(codice, title, teacher)
        self._cod_counter += 1
        return codice

    def get_course_info(self, course_id: int) -> str:
        titolo = self._corsi[course_id].get_titolo()
        docente = self._corsi[course_id].get_docente()
        return str(course_id) + "," + titolo + "," + docente

    # R4
    def register_to_course(self, student_id: int, course_id: int) -> None:
        nome = self._studenti[student_id].get_nome()
        cognome = self._studenti[student_id].get_cognome()
        titolo = self._corsi[course_id].get_titolo()
        docente = self._corsi[course_id].get_docente()
        self._corsi[course_id].add_student(student_id, nome, cognome)
        self._studenti[student_id].add_corso(titolo, docente)

    def get_attendees(self, course_id: int) -> str:
        studenti = self._corsi[course_id].get_students()
        elenco = ""
        for s in studenti:
            elenco = elenco + "\n" + str(studenti[s].get_matricola()) + " " + str(studenti[s].get_nome()) + " " + str(studenti[s].get_cognome())
        return elenco

    def get_study_plan(self, student_id: int) -> List[str]:
        corsi = self._studenti[student_id].get_corsi()
        elenco = []
        for c in corsi:
            elenco.append(str(corsi[c].get_cod()) + "," + str(corsi[c].get_titolo()) + "," + str(corsi[c].get_docente()))
        return elenco
