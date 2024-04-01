import tkinter as tk
from tkinter import messagebox
from consts import LONGUEUR, HAUTEUR , COULEUR_PRINCIPALE, COULEUR_BOUTON,COULEUR_TEXT_BOUTON
from model.player import Player
from model.round import Round
from view.game_screen.score import Score
from view.game_screen.interface_jeu import InterfaceJeu
"""
# La classe RegleClassique est la classe qui démarre à chaque nouveau tour et qui met fin au jeu si un joueur remporte 5 manches.

# La classe JeuClassique gère le déroulement d'une manche ;elle commence par la fonction commencer_tour(self)
qui initialise le joueur courantet vérifie que la pioche n'est pas vide et qu'il y a des possibilités de jouer.
Tant que c'est le cas, elle affiche les cartes du joueur courant.Dans le cas où le joueur courant a été attaqué,
elle désactive tous les boutons de mouvement et active le bouton de dévance pour qu'il se défende.
Si la pioche est vide ou s'il n'y a pas de possibilité de jouer, elle va directement vers la fonction verifier_gagne
qui teste les possibilités de gagner.Le joueur commence par choisir le type de mouvement, cela se fait en cliquant sur le bouton.
Lorsqu'il clique, la commande du bouton va appeler la fonction obtenir_possibilites qui va vérifier les possibilités de ce mouvement 
et mettre à jour les cartes en fonction des possibilités.Si aucune possibilité n'est trouvée, toutes les cartes sont désactivées.
Pour l'attaque : s'il a la possibilité d'attaquer avec deux cartes à la fois,on affiche un message lui demandant s'il veut attaquer avec deux cartes ou non.
S'il le souhaite, il doit cliquer sur deux cartes, sinon il doit en cliquer une seule.
Si de base, il n'a même pas la possibilité d'attaquer avec deux cartes,le message n'est pas affiché.
Une fois que le joueur a attaqué, le rôle passe à l'autre joueur qui a seulement la possibilité de se défendre
(les autres boutons sont désactivés pour lui).Il clique sur Dévance, et s'il a la possibilité de le faire, il se défend,
que l'attaque ait été en deux ou en une carte.S'il n'a pas la possibilité de se défendre, le joueur attaquant remporte la manche,
et il commencera la nouvelle manche (le joueur gagnant commence toujours la nouvelle manche).Lorsqu'un joueur remporte 5 manches, 
le jeu se termine,et on affiche un message demandant s'ils veulent encore jouer un autre jeu.
"""

class JeuClassique:
    def __init__(self, root, tour, enterface , regle_classique):
        self.turn_text = None
        self.root: tk.Tk = root
        self.round = tour
        self.interface = enterface
        self.canvas = self.interface.canvas
        self.regle_classique = regle_classique
        self.nb_cart = None
        self.nb_attq = 0  # Variable pour enregistrer la façon d'attaquer (soit 1 carte ou 2 cartes). On va aussi l'utiliser pour la défense de l'autre joueur.
                # Si l'attaque précédente est une attaque simple, l'autre joueur ne peut faire que la défense.
        self.nb_type_attq = 0
        self.dev = 0 #vraibles pour indiquer que il doit defander
        self.bot_devance = tk.Button(self.canvas, width=7, height=2, text="Devancer", state=tk.DISABLED,
                                       command=self.click_devance,bg=COULEUR_BOUTON, fg=COULEUR_TEXT_BOUTON, 
                                       font=("Palatino Linotype", 12, "bold"))
        self.bot_devance.place(relx=0.51, rely=0.92, anchor="center")


        self.interface.choix_move.bind(self.obtenir_possibilites)
        self.interface.bouton_carte.bind(self.on_click_button_carte)

    def on_click_button_carte(self):
        self.affect_move()
        self.interface.plateau.move_joueur(self.jouer_courant)
        if self.nb_cart is not None:
            self.jouer_carte() # on change le joueur  apres le joueur courante joue

    def commencer_tour(self):
        self.jouer_courant = self.round.players[self.round.current_turn]

        if (len(self.round.paquet_pioche) and self.jouer_courant.possibilities()) :
            #D'abord, on regarde s'il y a une attaque effectuée par l'autre joueur.
            #Ici, on force le joueur courant à devancer en attaquant le même nombre de cartes.
            if (self.nb_attq != 0 ):
                #on active le button devance 
                self.bot_devance.config(state=tk.NORMAL)
                #On désactive les autres boutons de choix.
                self.interface.choix_move.boutons[0].config(state=tk.DISABLED)
                self.interface.choix_move.boutons[1].config(state=tk.DISABLED)
                self.interface.choix_move.boutons[2].config(state=tk.DISABLED)
            
            
            self.affiche_jouer(self.jouer_courant)
            self.afficher_cartes()  # afficher les carte de jouer courant
        else:
            #self.round.update_possibilities(self.round.players[1 - self.round.current_turn])
            self.verifie_gangant()  # veriffier les possibilte de gange
            

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
        # dans le cas d'une attaque, le joueur choisit la façon d'attaquer selon ses cartes d'attaque 
        if self.interface.choix_move.type == 3:
            self.type_attaque(self.round , possibilites)

    #on regestre le type d'attaque dans une variable temporair pour gerer le nombre des clicks sur les cartes d'attaque 
    def type_attaque(self,tour,possibilite):
        if len(possibilite) > 1:
            answer = messagebox.askyesno("Question", "Voulez-vous forcer votre attaque avec deux cartes par joue ?")
            if answer:
                self.nb_type_attq = 2
            else:
                self.nb_type_attq =1
        else :
            self.nb_type_attq =1

    def obtenir_possibilites_reelles(self):
        if self.interface.choix_move.type == 1:
            return self.jouer_courant.avance_possible # return possibilte d'avance
        elif self.interface.choix_move.type == 2:
            return self.jouer_courant.retour_possible  #retourn possibilite de recule
        elif self.interface.choix_move.type == 3:
            return self.jouer_courant.attaque_possible  # retourn possibiblite d'attaque
        else:
            return []

    def affect_move(self):
        if (self.interface.choix_move.type is not None) or (self.dev):
            if self.dev :
                self.devance()

            elif self.interface.choix_move.type == 3:
                self.attaque()
            else:
                """On change le sens du nombre de cartes selon le joueur, car le joueur 1 voit sa position
                   croissante en avançant et décroissante en reculant. D'autre part, le joueur 2 voit sa position
                   en avançant décroissante et croissante en reculant.
                """
                if self.interface.choix_move.type == 1:
                    if self.round.current_turn == 1:
                        self.nb_cart = -self.interface.bouton_carte.nb_move
                    else:
                        self.nb_cart = self.interface.bouton_carte.nb_move
            
                elif self.interface.choix_move.type == 2:
                    if self.round.current_turn == 0:
                        self.nb_cart = -self.interface.bouton_carte.nb_move
                    else:
                        self.nb_cart = self.interface.bouton_carte.nb_move

                self.jouer_courant.avancer(self.nb_cart)
                self.interface.choix_move.type = None
                #on reintailse le type a None pour eviter de effectuer un mouvement au prochin tour sans choisi le type 
        else:
            messagebox.showerror("Erreur","Oops,Vous devriez d'abord choisir le type de mouvement à effectuer.")

    def attaque(self):
        if (self.nb_attq +1  < self.nb_type_attq  ):
            self.nb_attq += 1
            #on prend deux cartes de la liste des cartes 
            prem_carte = self.interface.bouton_carte.nb_move
            self.round.piocher(self.jouer_courant, prem_carte) #on suprime la premier carte
        else : 
            self.nb_attq += 1
            self.nb_cart = self.interface.bouton_carte.nb_move
            self.interface.choix_move.type = None
        # On réinitialise le type à None après avoir terminé toutes les attaques
        # pour éviter de passer au prochain tour sans choisir les nombres de cartes que le joueur souhaite pour l'attaque

        self.jouer_courant.avancer(0) #On met 0 pour le mouvement, car le joueur ne bouge pas en attaque.
        

    def attaque_reusi(self, joueur):
        joueur.score += 1
        messagebox.showinfo("Information", f"Oops, vous n'avez pas la possibilité de vous défendre, donc {joueur.nom } a remporté la manche .")
        self.interface.score.update_score(self.round)
        self.interface.choix_move.type = None
        # Tant que l'attaque réussit, on réinitialise tout à nouveau
        self.nb_attq = 0
        self.dev = 0 # on anule la possibilte de devance , pour que la prochain tour ne commence pas par devance
        self.bot_devance.config(state=tk.DISABLED) #apres fin defavance on desactive le button devance 
        self.interface.choix_move.boutons[0].config(state=tk.NORMAL) #on reactive les buttons des move 
        self.interface.choix_move.boutons[1].config(state=tk.NORMAL)
        self.interface.choix_move.boutons[2].config(state=tk.NORMAL) 
                 
        #si l'attaque reusit , donc on retour le parol du joueur gangée
        self.round.current_turn = 1 - self.round.current_turn
        self.jouer_courant = self.round.players[self.round.current_turn] 
        #aller vers intialse le jeu 
        self.regle_classique.demarer()

    def devance(self):
        if (self.nb_attq == 2 ):
            prem_carte = self.interface.bouton_carte.nb_move
            self.round.piocher(self.jouer_courant, prem_carte) #on suprime la premier carte 
            self.nb_attq -= 1
        else:
            self.nb_cart = self.interface.bouton_carte.nb_move
            # Tant que la devance réussit, on réinitialise tout à nouveau
            self.nb_attq = 0 
            self.interface.choix_move.type = None
            self.dev = 0
            self.bot_devance.config(state=tk.DISABLED) 
            self.interface.choix_move.boutons[0].config(state=tk.NORMAL) 
            self.interface.choix_move.boutons[1].config(state=tk.NORMAL)
            self.interface.choix_move.boutons[2].config(state=tk.NORMAL)

        self.jouer_courant.avancer(0) #On met 0 pour le mouvement, car le joueur ne bouge pas en attaque.
        

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

    
    def verifie_gangant(self):
        if self.jouer_courant.possibilities() == 0:
            # si le jouer ne peux pas effect un move donc l'autre jouer a ganger
            self.round.players[1 - self.round.current_turn].score += 1
            messagebox.showinfo("Information", f"{self.round.players[1 - self.round.current_turn].nom } a remporté la manche, car vous n'avez pas des possibilités de jouer")
        elif not self.round.paquet_pioche:
            # si les cartes pioche finis on regarde le postiones de jouers le plus avancer gange
            # pour savoir qui le plus avancer on calcule la distance derier chaqun
            """
            if self.jouer_courant.attaque_possible :
                #On désactive les autres boutons de choix. on garde juste l'attaque 
                self.interface.choix_move.boutons[0].config(state=tk.DISABLED)
                self.interface.choix_move.boutons[1].config(state=tk.DISABLED)
                self.chance_devance = 1
            """
            if ( self.nb_attq != 0):
                #Dans le cas où un joueur effectue une attaque et que la pioche est vide, donc il gagne , 
                # comme le joueur courant change apres l'attaque. on changer le joueur ici 
                self.round.players[1 - self.round.current_turn].score += 1
                messagebox.showinfo("Information", f"{self.round.players[1 - self.round.current_turn].nom } a attaqué et la pioche est vide, donc il a remporté la manche.")

            elif ( len(self.round.players[0].attaque_possible) > len(self.round.players[1].attaque_possible)) :
                self.round.players[0].score += 1
                messagebox.showinfo("Information", f"La pioche est vide, puisque {self.round.players[0].nom} a plus de possibilités d'attaque ( { self.round.players[0].attaque_possible } ), il remporte la manche.")

            elif( len(self.round.players[1].attaque_possible) >len(self.round.players[0].attaque_possible) ) :
                self.round.players[1].score += 1
                messagebox.showinfo("Information", f"La pioche est vide, puisque {self.round.players[1].nom } a plus de possibilités d'attaque ( { self.round.players[1].attaque_possible } ), il remporte la manche.")
                
            else:
                #on cherche le joueur le plus avancer sur la plateau
                dis_arier_1 = self.round.players[0].position
                dis_arier_2 = 22 - self.round.players[1].position
                if dis_arier_1 > dis_arier_2:
                    self.round.players[0].score += 1
                    messagebox.showinfo("Information", f"La pioche est vide, puisque {self.round.players[0].nom } est plus avancé sur le plateau ( position = {self.round.players[0].position } ) , il a remporté la manche.")
                elif dis_arier_2 > dis_arier_1:
                    self.round.players[1].score += 1
                    messagebox.showinfo("Information", f"La pioche est vide, puisque {self.round.players[1].nom } est plus avancé sur le plateau ( position = {self.round.players[1].position } ), il a remporté la manche.")
                # c'est imposible que la distance derier les deux joueur soit egeux ( car on la taille impair pour 
                #  le plateu de jeu qui egale 23) donc pas la pien de faire else 

            
        self.interface.score.update_score(self.round)
        self.interface.choix_move.type = None
        # Tant que la tour finit , on réinitialise tout à nouveau
        self.nb_attq = 0
        self.bot_devance.config(state=tk.DISABLED) #apres fin defavance on desactive le button devance 
        self.interface.choix_move.boutons[0].config(state=tk.NORMAL) #on reactive les buttons des move 
        self.interface.choix_move.boutons[1].config(state=tk.NORMAL)
        self.interface.choix_move.boutons[2].config(state=tk.NORMAL)  
                
        self.regle_classique.demarer()

    # Lorsqu'il clique sur "devancer", on examine ses possibilités de défense.
    # S'il n'a pas de possibilités de défense, on passe à la fonction "attaque_reussie"
    # qui augmente le score de l'autre joueur et réinitialise tout à nouveau.
    def click_devance(self):
        self.dev = 1
        possib_dev = self.jouer_courant.attaque_possible # les possibilite de devance c'est le meme d'attaque 
        self.interface.bouton_carte.update_carte(self.canvas, self.jouer_courant.cartes, possib_dev)
        #On regarde d'abord s'il y a des possibilités de dévance 
        if(self.nb_attq == 2 ):
            if(len(self.jouer_courant.attaque_possible) < 2 ):
                self.attaque_reusi( self.round.players[1-self.round.current_turn] )
        elif(self.nb_attq == 1) :
            if(len(self.jouer_courant.attaque_possible) < 1 ):
                self.attaque_reusi( self.round.players[1-self.round.current_turn] )


#---------------- La classe pour le déroulement du jeu jusqu'à ce qu'un joueur gagne 5 manches -----------------------
class RegleClassique:
    def __init__(self, root, plan, photo_1, photo_2,nom_1,nom_2):
        self.root = root
        self.joueur_1 = Player(nom_1, photo_1, 0)
        self.joueur_2 = Player(nom_2, photo_2, 1)
        self.tour = Round([self.joueur_1, self.joueur_2])
        self.interface = InterfaceJeu(self.root, plan, self.joueur_1, self.joueur_2, self.tour)
        self.jeu = JeuClassique(self.root, self.tour, self.interface , self )

    # le jeu finit quand un jouer a score 5
    # apres chaque tour on reintailise le jeu
    def demarer(self):
        if (self.tour.players[0].score < 5 ) and (self.tour.players[1].score < 5 ):
            self.dev = 0
            self.jeu.round.init_round()
            self.interface.plateau.intiale_case(self.tour.players[0],self.tour.players[1])
            self.interface.pioche.intialse_pioche(self.tour.paquet_pioche)
            self.jeu.commencer_tour()
        else:
            if self.tour.players[0].score == 5:
                messagebox.showinfo("Information", f"Le joueur {self.tour.players[0].nom } a gagné le jeu .")
            else:
                messagebox.showinfo("Information", f"Le joueur {self.tour.players[1].nom } a gagné le jeu .")
 
            answer = messagebox.askyesno("Question", "Voulez-vous continuer?")
            if answer:
                #initialise les score a 0 et update le leble de score 
                self.jeu.round.init_score()
                self.interface.score.update_score(self.jeu.round)
                self.jeu.round.current_turn = 0
                self.demarer()
            else:
                self.root.event_generate("<<retour_clicked>>")


def PageJeuClassique(root,plan,phot_1 , phot_2 ,nom_1 , nom_2 ):
    jeu_classique = RegleClassique(root,plan,phot_1,phot_2,nom_1,nom_2)
    jeu_classique.demarer()



