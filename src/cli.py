from model.player import Player
from model.round import Round


class BasicRule:
    def __init__(self, tour):
        self.round: Round = tour

    def jouer_Tour(self):

        player = self.round.players[self.round.current_turn]
        # print("UUUUUUUUUUUUUUUUUUU")

        while len(self.round.paquet_pioche) and player.possibilities():

            # print("#########################################")

            print(f"player {player.nom}: Position = {player.position} | Score = {player.score}")

            print(f"Cartes du player {player.nom}: {', '.join(map(str, player.cartes))}")
            self.round.print_possibilities(player)

            mode_move = input("Avancer (v), Attaquer (t) ou Reculer (r) : ")
            while mode_move not in ['v', 't', 'r']:
                print("votre choix n'est pas valide")
                mode_move = input("Avancer (v), Attaquer (t) ou Reculer (r) : ")

            if mode_move == 't':
                print("Attaque réussie ! ", player.nom, "gagne le Tour !")
                player.score += 1
                return

            elif mode_move == 'v':
                nb_move = int(input("Déplacement (entier positif ou nul) : "))
                while nb_move not in self.round.players[self.round.current_turn].avance_possible:
                    print("votre choise pas correct ")
                    nb_move = int(input("Déplacement (entier positif ou nul) : "))

                if self.round.current_turn:
                    nb_move = -nb_move
                    player.avancer(nb_move)

                else:
                    player.avancer(nb_move)

            elif mode_move == 'r':
                nb_move = int(input("Déplacement (entier positif ou nul) : "))
                while nb_move not in self.round.players[self.round.current_turn].reTour_possible:
                    print("votre choise pas correct ")
                    nb_move = int(input("Déplacement (entier positif ou nul) : "))

                if self.round.current_turn:
                    player.avancer(nb_move)

                else:
                    nb_move = -nb_move
                    player.avancer(nb_move)

            self.round.piocher(player, abs(nb_move))

            self.round.current_turn = 1 - self.round.current_turn
            player = self.round.players[self.round.current_turn]
            self.round.print_possibilities(player)
            self.round.update_possibilities(player)
            self.round.print_possibilities(player)

            print(player.possibilities())


class EnGardeGame:
    def __init__(self, nom1, nom2):
        player1 = Player(nom1)
        player2 = Player(nom2)
        self.tour = Round([player1, player2])
        self.rule = BasicRule(self.tour)

    def jouer_partie(self):
        while max(player.score for player in self.tour.players) < 5 and self.tour.paquet_pioche:
            self.rule.round.init_round()
            self.rule.jouer_Tour()

        gagnant = max(self.tour.players, key=lambda player: player.score)
        print(f"Le player {gagnant.nom} remporte la partie avec un score de {gagnant.score} !")


def main():
    jeu = EnGardeGame("Abdullah", "Emad")
    jeu.jouer_partie()


if __name__ == "__main__":
    main()
