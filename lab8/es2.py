# Creare la classe File rappresentante un generico file vuoto.
# Il costruttore deve accettare come unico parametro il nome del file.
# Creare tre getter: get_name(self), get_dim(self) e get_info(self).
# Il primo restituisce il nome del file e il secondo la sua dimensione (zero in quanto vuoto).
# get_info(self) restituisce una stringa contenente sia il nome che la dimensione del file.
# Per ottenerli DEVE usare i metodi get_name(self) e get_dim(self).
# Scrivere il metodo __repr__(self) che restituisca il contenuto del file, in questo caso una stringa vuota.

# Notare che anche il metodo get_info(self) cambia comportamento, perché nonostante non venga fatto l'override esplicito
# esso utilizza metodi di cui invece viene fatto.

class File:
    def __init__(self, nome):
        self.nome = nome
        self.dim = 0
        self.contenuto = ""

    def get_name(self):
        return self.nome

    def get_dim(self):
        return self.dim

    def get_info(self):
        nome = self.get_name()
        dim = self.get_dim()
        ris = "Nome: " + str(nome) + " , " + "Dimensione: " + str(dim)
        return ris

    def __repr__(self):
        return self.contenuto


# Creare la classe TextFile che eredita da File. Il costruttore, come il padre, accetta come unico parametro
# il nome del file. Scrivere il metodo add_line(self, str: line) che, passata una stringa, la aggiunga come
# nuova riga del file.
#
# Fare l'override dei metodi dim(self) e __repr(self)__ per restituire, rispettivamente, il numero di righe e
# una stringa rappresentante il contenuto del file.


class TextFile(File):
    def __init__(self, nome):
        super().__init__(nome)

    def add_line(self, line: str):
        self.contenuto = self.contenuto + line + "\n"

    def get_dim(self):
        nrighe = len(self.contenuto.split("\n")) - 1
        return nrighe

    def __repr__(self):
        return str(self.contenuto.strip())


# Creare la classe BitMap che eredita da File. Il costruttore accetta come parametri il nome del file e una tabella
# contenente numeri da 0 a 255 (non controllare correttezza) rappresentante i colori dell'immagine.
#
# Fare l'override del metodo dim(self) per restituire un tupla contenente le dimensioni dell'immagine.
# Fare l'override del metodo __repr__ per restituire una stringa rappresentate l'immagine, convertendo i numeri
# colore a esadecimale tramite la funzione hex().


class BitMap(File):
    def __init__(self, nome, tabella):
        super().__init__(nome)
        self.tabella = tabella

    def get_dim(self):
        d = len(self.tabella)  # DUBBIO
        return d

    def __repr__(self):
        ris = ""
        for n in self.tabella:
            ris = ris + str(hex(n))
        return ris


# Scrivere un main che crei almeno un'istanza per classe e verificare che i metodi di cui è stato fatto l'override
# si comportino in modo diverso tra le classi.

def main():
    t = TextFile("Alice")
    t.get_name()
    t.add_line("C'era una volta")
    t.add_line("una bambina di nome Alice")
    t.add_line("che entrò nella tana del Bianconiglio.")
    t.add_line("Il paese delle Meraviglie era enorme")
    print("Numero di linee del testo", t.get_dim())
    print(t.__repr__())
    print(t.get_info())
    print("-------")
    t = [0, 22, 25, 50, 75, 255]
    i = BitMap("ciao", t)
    print("Dimensione dell'immagine: ", i.get_dim())
    print(i.__repr__())
    print(i.get_info())


# main()
