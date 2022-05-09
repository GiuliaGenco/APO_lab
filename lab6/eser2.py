# Scrivere una classe che rappresenti un documento d'identità.
#
# Il costruttore deve accettare come parametro il nome e il cognome dell'intestatario e
# opzionalmente l'anno in cui il documento è stato rilasciato. Se non specificato usare 2022 come valore di default.
#
# Scrivere i getters per nome, cognome e anno di rilascio.
#
# Scrivere il metodo set_birth_year che permetta registrare l'anno di nascita.
# Se l'anno di nascita è maggiore dell'anno di rilascio l'anno di nascita deve essere impostato
# uguale all'anno di rilascio. Scrivere un getter per ottenere l'anno di nascita.
#
# Il costruttore deve definire un ulteriore attributo, rappresentante il numero documento.
# Il numero documento deve incrementare di uno per ogni nuovo documento.
# Il numero documento deve essere ottenibile tramite getter.
#
# Scrivere una funzione main che testi le funzionalità della classe sviluppata.
#
# Suggerimento: per aggiornare il numero documento si può usare una proprietà di classe
# che tiene conto di quante volte il costruttore viene chiamato.

class Documento:

    nuovo_documento = 1

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.anno = 2022
        self.annoNascita = 0
        self.ndocumento = Documento.nuovo_documento
        Documento.nuovo_documento += 1

    def get_nome(self):
        nome = self.nome
        print("Nome: ", nome)
        return nome

    def get_cognome(self):
        cognome = self.cognome
        print("Cognome: ", cognome)
        return cognome

    def get_anno(self):
        anno = int(self.anno)
        # print("Anno di registrazione: ", anno)
        return anno

    def set_birth_year(self, year):
        # Se l'anno di nascita è maggiore dell'anno di rilascio, l'anno di nascita deve essere impostato
        # uguale all'anno di rilascio.
        annocarta = self.get_anno()
        if year > annocarta:
            self.annoNascita = annocarta
            print("ERRORE: l'anno inserito è maggiore del corrente.")
        else:
            self.annoNascita = int(year)

    def get_anno_nascita(self):
        year = int(self.annoNascita)
        print("Anno di nascita: ", year)
        return year

    def get_ndocumento(self):
        ndocu = self.ndocumento
        print("Numero documento attuale: ", ndocu)
        return ndocu


def main():
    d = Documento("Paolo", "Sieni Miceli")
    d.get_nome()
    d.get_cognome()
    d.set_birth_year(1998)
    d.get_anno_nascita()
    d.get_anno()
    d.get_ndocumento()

    g = Documento("Giulia", "Genco")
    g.get_ndocumento()

    f = Documento("Camilla", "De Angelis")
    f.get_ndocumento()


main()
