import tkinter as tk
from tkinter import messagebox
from consts import LONGUEUR, COULEUR_PRINCIPALE, HAUTEUR
from model.player import Player
from model.round import Round
from view.game_screen.score import Score
from view.game_screen.interface_jeu import InterfaceJeu
"""
# La classe RegleBasic est la classe qui démarre à chaque nouveau tour et qui met fin au jeu si un joueur remporte 5 manches.

# La classe Jeu gère le déroulement d'une manche ;elle commence par la fonction commencer_tour(self)
qui initialise le joueur courantet vérifie que la pioche n'est pas vide et qu'il y a des possibilités de jouer.
Tant que c'est le cas, elle affiche les cartes du joueur courant.
Si la pioche est vide ou s'il n'y a pas de possibilité de jouer, elle va directement vers la fonction verifier_gagne
qui teste les possibilités de gagner.Le joueur commence par choisir le type de mouvement, cela se fait en cliquant sur le bouton.
Lorsqu'il clique, la commande du bouton va appeler la fonction obtenir_possibilites qui va vérifier les possibilités de ce mouvement 
et mettre à jour les cartes en fonction des possibilités.Si aucune possibilité n'est trouvée, toutes les cartes sont désactivées.
Pour l'attaque :lorsqu'un joueur attaque , il remporte la manche et commence le nouveau tour.
Lorsqu'un joueur remporte 5 manches, le jeu se termine,et on affiche un message demandant s'ils veulent encore jouer un autre jeu.
"""

class Jeu:
    def __init__(self, root, tour, enterface , regle_basic):
        self.turn_text = None
        self.root: tk.Tk = root
        self.round = tour
        self.interface = enterface
        self.canvas = self.interface.canvas
        self.regle_basic = regle_basic
        self.nb_cart = None

        self.interface.choix_move.bind(self.obtenir_possibilites)
        self.interface.bouton_carte.bind(self.on_click_button_carte)

    def on_click_button_carte(self):
        self.affect_move()
        self.interface.plateau.move_joueur(self.jouer_courant)
        if self.nb_cart is not None:
            self.jouer_carte() # on change le joueur  apres le joueur courante joue 

    def commencer_tour(self):
        self.jouer_courant = self.round.players[self.round.current_turn]
        if len(self.round.paquet_pioche) and self.jouer_courant.possibilities():
            self.affiche_jouer(self.jouer_courant)
            self.afficher_cartes()  # afficher les cartes de joueur courant
        else:
            self.verifie_gangant(self.round)  # veriffier les possibilte de gange
            

    def affiche_jouer(self, jouer):
        if self.turn_text:
            self.canvas.delete(self.turn_text)
        tex = f"Le tour de {jouer.nom}"
        self.turn_text = self.canvas.create_text(920, 180, text=tex, font=("Comic Sans MS", 25, "bold italic"),
                                                 fill="black")

    def afficher_cartes(self):
        self.interface.bouton_carte.create_butt_carte(self.canvas, self.jouer_courant.cartes)

    def obtenir_possibilites(self):
        possibilites = self.obtenir_possibilites_reelles()
        self.interface.bouton_carte.update_carte(self.canvas, self.jouer_courant.cartes, possibilites)
        if len(possibilites) == 0:
            messagebox.showerror("Erreur","Oops, vous ne pouvez pas effectuer ce mouvement ; veuillez choisir un autre mouvement.")


    def obtenir_possibilites_reelles(self):
        if self.interface.choix_move.type == 1:
            return self.jouer_courant.avance_possible # return possibilte d'avance 
        elif self.interface.choix_move.type == 2:
            return self.jouer_courant.retour_possible #retourn possibilite de recule
        elif self.interface.choix_move.type == 3:
            return self.jouer_courant.attaque_possible # retourn possibiblite d'attaque
        else:
            return []

    def affect_move(self):
        if self.interface.choix_move.type is None:
            messagebox.showerror("Erreur","Oops,Vous devriez d'abord choisir le type de mouvement à effectuer.")
        else:
            if self.interface.choix_move.type == 3:
                #si il effect un attaque il gange dircte
                self.jouer_courant.score += 1
                messagebox.showinfo("Information", f"{self.jouer_courant.nom } a remporté la manche car il a effectué une attaque .")
                self.interface.score.update_score(self.round)
                self.interface.choix_move.type = None
                #aller vers intialse le jeu 
                self.regle_basic.demarer()
            else:
                """On change le sens du nombre de cartes selon le joueur, car le joueur 1 voit sa position
                   croissante en avançant et décroissante en reculant. D'autre part, le joueur 2 voit sa position
                   en avançant décroissante et croissante en reculant.
                """
                if self.interface.choix_move.type == 1: # pour cas cas avancer
                    if self.round.current_turn == 1:
                        self.nb_cart = -self.interface.bouton_carte.nb_move
                    else:
                        self.nb_cart = self.interface.bouton_carte.nb_move
            
                elif self.interface.choix_move.type == 2: # pour cas reculer 
                    if self.round.current_turn == 0:
                        self.nb_cart = -self.interface.bouton_carte.nb_move
                    else:
                        self.nb_cart = self.interface.bouton_carte.nb_move

                self.jouer_courant.avancer(self.nb_cart)
                self.interface.choix_move.type = None
                #on reintailse le type a None pour eviter de effectuer un mouvement au prochin tour sans choisi le type 

    def jouer_carte(self):
        self.nb_cart = abs(self.nb_cart)
        self.round.piocher(self.jouer_courant, self.nb_cart)
        self.interface.pioche.carte_pioche(self.round.paquet_pioche)
        self.interface.pioche.carte_used(self.nb_cart)
        self.round.current_turn = 1 - self.round.current_turn
        self.jouer_courant = self.round.players[self.round.current_turn]
        self.round.update_possibilities(self.jouer_courant)
        self.nb_cart = None # on reitialise le carte a None pour pas entrer en cette fonction sans affecte un correct mouvment 
        self.commencer_tour()

    def verifie_gangant(self, tour):
        if self.jouer_courant.possibilities() == 0:
            # si le jouer ne peux pas effect un move donc l'autre jouer a ganger
            self.round.players[1 - self.round.current_turn].score += 1
            messagebox.showinfo("Information", f"{self.round.players[1 - self.round.current_turn].nom } a remporté la manche, car vous n'avez pas des possibilités de jouer.")
        elif not self.round.paquet_pioche:
            # si les cartes pioche finis on regarde le postiones de jouers le plus avancer gange
            # pour savoir qui le plus avancer on calcule la distance derier chaqun
            dis_arier_1 = self.round.players[0].position
            dis_arier_2 = 22 - self.round.players[1].position

            if dis_arier_1 > dis_arier_2:
                self.round.players[0].score += 1
                messagebox.showinfo("Information", f"La pioche est vide, puisque {self.round.players[0].nom } est plus avancé sur le plateau ( position = {self.round.players[0].position } ), il a remporté la manche .")
            elif dis_arier_2 > dis_arier_1:
                self.round.players[1].score += 1
                messagebox.showinfo("Information", f"La pioche est vide, puisque {self.round.players[1].nom } est plus avancé sur le plateau ( position = {self.round.players[1].position } ), il a remporté la manche.")
            # c'est imposible que la distance derier les deux joueur soit egeux ( car on la taille impair pour
            #  le plateu de jeu qui egale 23) donc pas la pien de faire else 


        self.interface.score.update_score(self.round)
        self.interface.choix_move.type = None
        self.regle_basic.demarer()


#---------------- La classe pour le déroulement du jeu jusqu'à ce qu'un joueur gagne 5 manches -----------------------
class RegleBasic:
    def __init__(self, root, plan, photo_1, photo_2,nom_1,nom_2):
        self.root = root
        self.joueur_1 = Player(nom_1, photo_1, 0)
        self.joueur_2 = Player(nom_2, photo_2, 1)
        self.tour = Round([self.joueur_1, self.joueur_2])
        self.interface = InterfaceJeu(self.root, plan, self.joueur_1, self.joueur_2, self.tour)
        self.jeu = Jeu(self.root, self.tour, self.interface , self )

    # le jeu finit quand un jouer a score 5
    # apres chaque tour on reintailise le jeu
    def demarer(self):
        if (self.tour.players[0].score < 5 ) and (self.tour.players[1].score < 5 ):
            self.jeu.round.init_round()
            self.interface.plateau.intiale_case(self.tour.players[0],self.tour.players[1])
            self.interface.pioche.intialse_pioche(self.tour.paquet_pioche)
            self.jeu.commencer_tour()
        else:
            if self.tour.players[0].score == 5:
                messagebox.showinfo("Information", f"{self.tour.players[0].nom } a gagné le jeu .")
            else:
                messagebox.showinfo("Information", f"{self.tour.players[1].nom } a gagné le jeu .")

            
            
            answer = messagebox.askyesno("Question", "Voulez-vous continuer?")
            if answer:
                #initialise les score a 0 et update le leble de score 
                self.jeu.round.init_score()
                self.interface.score.update_score(self.jeu.round)
                self.jeu.round.current_turn = 0
                self.demarer()
            else:
                self.root.event_generate("<<retour_clicked>>")


def PageJeuBasic(root,plan,phot_1 , phot_2 ,nom_1 , nom_2 ):
    jeu_basic = RegleBasic(root,plan,phot_1,phot_2,nom_1,nom_2)
    jeu_basic.demarer()
