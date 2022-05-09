# Creare la classe Player che rappresenti un giocatore.
# Il costruttore deve ricevere nome, cognome ed età del giocatore.
# Questi valori devono essere ottenibili tramite getters.
#
# Creare la classe Team che rappresenti una squadra.
# Il costruttore deve ricevere il nome della squadra e la città a cui appartiene.
# Questi valori devono essere ottenibili tramite getters.
#
# Il giocatore deve avere un metodo set_team che registra la squadra in cui gioca il giocatore.
# Il metodo riceve come parametro un oggetto della classe Team.
# Scrivere un getter della classe giocatore che restituisca il Team del giocatore.
# Se una squadra non è registrata deve restituire None.
#
# La squadra deve avere un metodo add_player che riceve un oggetto di tipo Player da aggiungere alla squadra.
# Il metodo get_players della squadra restituisce la lista di Players che giocano nella squadra.
#
# Scrivere una funzione main che testi le funzionalità delle classi, associando i giocatori alle squadre e viceversa

class Player:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = int(eta)
        self.team = None

    def get_nome(self):
        nome = self.nome
        # print("Nome: ", nome)
        return nome

    def get_cognome(self):
        cognome = self.cognome
        # print("Cognome: ", cognome)
        return cognome

    def get_eta(self):
        eta = int(self.eta)
        # print("Età: ", eta)
        return eta

    def set_team(self, team):
        self.team = team

    def get_team(self):
        team = self.team
        # print("Squadra registrata in giocatore :", team.get_nome_squadra(), team.get_citta())
        return team


class Team:
    def __init__(self, nome, citta):
        self.nome = nome
        self.citta = citta
        self.players = []

    def get_nome_squadra(self):
        nome = self.nome
        # print("Nome della squadra: ", nome)
        return nome

    def get_citta(self):
        citta = self.citta
        # print("Città della squadra: ", citta)
        return citta

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        giocatori = self.players
        return giocatori


def main():
    p1 = Player("Paolo", "Sieni Miceli", 23)
    print(p1.get_nome())
    print(p1.get_cognome())
    print(p1.get_eta())

    p2 = Player("Giulia", "Genco", 23)

    t1 = Team("Milan", "Milano")

    print("---- Squadra ----")
    print(t1.get_citta())
    print(t1.get_nome_squadra())
    print(t1.get_players())

    # creo associazione
    t1.add_player(p1)
    t1.add_player(p2)
    p1.set_team(t1)
    p2.set_team(t1)

    # verifico associazione squadra --> giocatori
    print("---- Giocatori della squadra ----")
    for p in t1.get_players():
        print(p.get_nome(), p.get_cognome())

    # verifico associazione giocatori --> squadra
    print("--- Squadre dei giocatori ---")
    print(p1.get_team().get_nome_squadra())
    print(p2.get_team().get_nome_squadra())


main()
