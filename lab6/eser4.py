# Scrivere la classe Matrix che rappresenti una matrice 2x2.
# Il costruttore deve ricevere come unico argomento una tabella rappresentante la matrice.
# Scrivere due getters che restituiscano il numero di righe e il numero di colonne.
# Implementare gli operatori __add__, __sub__, __mul__ di modo che effettuino la somma,
# differenza e prodotto riga-colonna di due matrici. Scrivere l'operatore __eq__ di modo che sia possibile
# verificare l'uguaglianza di due matrici.
# Implementare il metodo __str__ per fornire una rappresentazione in stringa della matrice.
# Scrivere una funzione main esegua operazioni tra oggetti della classe Matrix (+, -, *).
# Testare anche l'operatore di confronto (==) e la rappresentazione in str provando a stampare un oggetto Matrix.
tab = [[0, 1],
       [2, 3]]

tab1 = [[0, 1],
        [2, 3]]

tab2 = [
    [0, 0],
    [0, 0]
]


class Matrix:
    def __init__(self, tabella):
        self.tabella = tabella
        self.righe = [tabella[0], tabella[1]]
        self.colonne = []
        for i in range(2):
            for j in range(2):
                self.colonne.append([tabella[i][j], tabella[i - 1][j]])
        # METODO BECERO
        self.colonne.pop(3)
        self.colonne.pop(2)

    def __sub__(self, other):
        risultato = [[], []]
        nrighe1 = self.get_nrighe()
        nrighe2 = other.get_nrighe()
        riga1 = self.righe
        riga2 = other.righe
        if nrighe1 == nrighe2:
            for i in range(nrighe1):
                for j in range(nrighe1):
                    risultato[i].append(riga1[i][j] - riga2[i][j])
        return risultato

    def __add__(self, other):
        risultato = [[], []]
        nrighe1 = self.get_nrighe()
        nrighe2 = other.get_nrighe()
        riga1 = self.righe
        riga2 = other.righe
        if nrighe1 == nrighe2:
            for i in range(nrighe1):
                for j in range(nrighe1):
                    risultato[i].append(riga1[i][j] + riga2[i][j])
        return risultato

    def __mul__(self, other):
        risultato = [[], []]
        nrighe1 = self.get_nrighe()
        nrighe2 = other.get_nrighe()
        riga1 = self.righe
        riga2 = other.righe
        if nrighe1 == nrighe2:
            for i in range(nrighe1):
                for j in range(nrighe1):
                    risultato[i].append(riga1[i][j] * riga2[i][j])
        return risultato

    def __eq__(self, other):
        risultato = False
        nrighe1 = self.get_nrighe()
        nrighe2 = other.get_nrighe()
        ncol1 = self.get_nrcolonne()
        ncol2 = other.get_ncolonne()
        riga1 = self.righe
        riga2 = other.righe
        if nrighe1 == nrighe2 and ncol2 == ncol1:
            for i in range(nrighe1):
                for j in range(nrighe1):
                    if riga1[i][j] == riga2[i][j]:
                        risultato = True
                        print("Le due matrici sono uguali")
                    else:
                        risultato = False
                        print("Le due matrici sono diverse")
        return risultato

    # Implementare il metodo __str__ per fornire una rappresentazione in stringa della matrice.
    def __str__(self):
        risultato = ""
        nrighe = self.get_nrighe()
        riga = self.righe
        for i in range(nrighe):
            for j in range(nrighe):
                risultato = risultato + str(str(riga[i][j]) + " ")
        print(risultato)
        return risultato

    def get_nrighe(self):
        nrighe = len(self.righe)
        # print("Numero di righe: ", nrighe)
        return nrighe

    def get_nrcolonne(self):
        ncolonne = len(self.colonne)
        # print("Numero di colonne: ", ncolonne)
        return ncolonne

    def stampa(self):
        nrighe = self.get_nrighe()
        for i in range(nrighe):
            print("Righe: ", self.righe[i])

        ncol = self.get_nrcolonne()
        for i in range(ncol):
            print("Colonne: ", self.colonne[i])


m = Matrix(tab)
# m.stampa()
# m.get_nrighe()
# m.get_nrcolonne()

m2 = Matrix(tab2)

s = m + m2
print("Risultato somma: ", s)

d = m2 - m
print("Risultato differenza: ", d)

mol = m2 * m
print("Risultato moltiplicazione: ", mol)

print(tab == tab1)
print(tab == tab2)

stringa = str(m)
