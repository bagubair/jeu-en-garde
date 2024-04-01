import random


class Round:
    def __init__(self, players):
        self.current_turn = 0
        self.players = players
        self.paquet_pioche = None
        self._init_paquet()

    def _init_paquet(self):
        self.paquet_pioche = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        random.shuffle(self.paquet_pioche)  # melange les cartes

    def init_round(self):
        self._init_paquet()

        self.players[0].position = 0
        self.players[1].position = 22

        self.distribute_cards()

        self.players[0].avance_possible = self.players[0].cartes
        self.players[1].avance_possible = self.players[1].cartes

        self.players[0].retour_possible = []
        self.players[1].retour_possible = []

        self.players[0].attaque_possible = []
        self.players[1].attaque_possible = []

    def init_score(self):
        self.players[0].score = 0
        self.players[1].score = 0
    def piocher(self, player, nb_move):
        index = player.cartes.index(nb_move)
        del player.cartes[index]
        if len(self.paquet_pioche) != 0 : # on ajoute une carte pour le joueur seulement s'il y a encore des cartes en pioche
            player.cartes.append(self.draw_card())
        # dans le cas où la pioche est vide, on supprime simplement la carte de la main du joueur 
        # sans en ajouter une autre (pour la règle classique)

    def draw_card(self):
        if not self.paquet_pioche:
            print("Plus de cartes dans le paquet.")
            return 0
        card = self.paquet_pioche.pop(0)  # supprimer la carte de paquet pioche et return la carte
        return card

    def distribute_cards(self):
        self.players[0].cartes = []
        self.players[1].cartes = []
        for i in range(5):
            self.players[0].cartes.append(self.draw_card())
            self.players[1].cartes.append(self.draw_card())

    def update_possibilities(self, player):
        # on mis a jour les possibilites de l'autre jouer
        if self.current_turn == 1:
            distance_avant = (player.position - (self.players[1 - self.current_turn].position))
        else:
            distance_avant = (self.players[1 - self.current_turn].position - player.position)

        if self.current_turn == 0:
            distance_arriere = player.position
        else:
            distance_arriere = 22 - player.position

        player.avance_possible = [i for i in player.cartes if i < distance_avant]
        player.attaque_possible = [i for i in player.cartes if i == distance_avant]
        player.retour_possible = [i for i in player.cartes if i <= distance_arriere]

    def print_possibilities(self, player):
        print("Possibilités de", player.nom, ": Avance =", player.avance_possible, "Attaque =", player.attaque_possible,
              "ReTour =", player.reTour_possible)
