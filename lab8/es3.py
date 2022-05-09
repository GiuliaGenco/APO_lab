# In questo esercizio utilizzeremo le classi sviluppate nell'esercizio precedente in modo polimorfico.
#
# Creare la classe Directory rappresentante una cartella.
# Il costruttore accetta come unico parametro il nome della directory.
# Il metodo add_file(self, file) permette di aggiungere un file alla cartella.
#
# Il metodo open_files(self) stampa a schermo il contenuto di tutti i file contenuti nella cartella.
# Il metodo __repr__(self) stampa il nome della cartella e, sotto di esso, le informazioni (nome e dimensione)
# di tutti i file che contiene (chiamando get_info(self) su di essi).
#
# my_folder:
#         empty.info: 0
#         myimage.bmp: (3, 2)
#         mytext.txt: 3

# Scrivere una main che, utilizzando le classi dell'esercizio precedente, crei delle istanze di diversi tipi di file
# e li aggiunga a un oggetto Directory.
#
# Notare che il codice che viene scritto per open_files(self) e __repr__(self)
# non è a conoscenza del tipo di file su cui opera, ma si comporta lo stesso diversamente a secondo del
# tipo di file su cui sta agendo. Questa è l'utilità del polimorfismo.

from es2 import TextFile
from es2 import BitMap


class Directory:
    def __init__(self, indirizzo):
        self._indirizzo = indirizzo
        self._cartella = []

    def add_file(self, file):
        self._cartella.append(file)

    def open_files(self):
        return print(self._cartella)

    def __repr__(self):
        print(self._indirizzo + ":")
        ris = ""
        for f in self._cartella:
            ris = ris + f.get_info() + "\n"
        return print(ris)


def main():
    # Scrivere una main che, utilizzando le classi dell'esercizio precedente, crei delle istanze di diversi tipi di file
    # e li aggiunga a un oggetto Directory.
    t = TextFile("Alice")
    t.add_line("C'era una volta")
    t.add_line("una bambina di nome Alice")
    t.add_line("che entrò nella tana del Bianconiglio.")
    t.add_line("Il paese delle Meraviglie era enorme")
    d = Directory("my_folder")
    d.add_file(t)

    t = [0, 22, 25, 50, 75, 255]
    i = BitMap("ciao", t)
    d.add_file(i)
    d.__repr__()


main()
