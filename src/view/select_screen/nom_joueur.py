import tkinter as tk
from consts import  COULEUR_BOUTON,COULEUR_TEXT_BOUTON
"""
    La classe NomJoueur permet aux joueurs de saisir leurs noms.
    Nous avons d'abord un label qui est lié à un événement de clic (si les joueurs veulent simplement entrer leurs noms).
    Ensuite, nous avons une zone de saisie (Entry) pour entrer les noms et, enfin, pour valider les noms.
    Toujours, nous avons deux fois tous les éléments, chacun pour un joueur. Donc, les fonctions ici sont globales pour les deux.
    Parametres des fonction :
    lab_nom: on indique le label.
    nb_j: c'est le nombre du joueur qu'il a saisi.
    frame: le cadre sur lequel la zone de saisie existe.
    zone: la zone de nom.
    bouton: le bouton pour valider le nom ; on le prend pour le masquer après la fin de la saisie du nom.
"""
class NomJouer:
    def __init__(self, canvas):
        # --------------------- définir les frame pour met le zone entry de saisir dans -------------
        self.frame_nom_1 = tk.Frame(canvas, width=300, height=100 , bg=COULEUR_BOUTON)
        self.frame_nom_1.place(relx=0.15, rely=0.50, anchor="center")
        self.frame_nom_2 = tk.Frame(canvas, width=300, height=70 , bg=COULEUR_BOUTON)
        self.frame_nom_2.place(relx=0.85, rely=0.50, anchor="center")
        # --------------------- définir le label -----------------------------------------------------
        self.label_nom_1 = tk.Label(self.frame_nom_1, text="Cliquez ici pour saisir nom de jouer 1",
                             font=("Palatino Linotype", 9) , bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.label_nom_1.pack(pady=20)
        self.label_nom_2 = tk.Label(self.frame_nom_2, text="Cliquez ici pour saisir nom de jouer 2",
                             font=("Palatino Linotype", 9) , bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.label_nom_2.pack(pady=20)
        # --------------------- enregistrer les noms entres des jouers -------------------------------
        self.nom_1 = "Joueur 1"  # ici on donne les noms des joueur par defut si les joueur ne rentrent pas des noms par clavier 
        self.nom_2 = "Joueur 2"
        # --------------------- définir l'event qui afiche la zone Entry -----------------------------
        self.label_nom_1.bind("<Button-1>", lambda event: self.afficher_zone_saisie(self.label_nom_1, self.zone_nom_1,
                                                                                    self.bouton_valider_1))
        self.label_nom_2.bind("<Button-1>", lambda event: self.afficher_zone_saisie(self.label_nom_2, self.zone_nom_2,
                                                                                    self.bouton_valider_2))
        # --------------------- définir les zones entry pour saisir les nom --------------------------
        self.zone_nom_1 = tk.Entry(self.frame_nom_1, font=("Palatino Linotype", 12), justify="center" , bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.bouton_valider_1 = tk.Button(self.frame_nom_1, text="Valider", bg=COULEUR_TEXT_BOUTON ,fg=COULEUR_BOUTON,
                            command=lambda: self.valider_nom(1, self.frame_nom_1,self.zone_nom_1,self.bouton_valider_1))

        self.zone_nom_2 = tk.Entry(self.frame_nom_2, font=("Palatino Linotype", 12), justify="center" , bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.bouton_valider_2 = tk.Button(self.frame_nom_2, text="Valider",bg=COULEUR_TEXT_BOUTON ,fg=COULEUR_BOUTON,
                            command=lambda: self.valider_nom(2, self.frame_nom_2,self.zone_nom_2, self.bouton_valider_2))
        

    def afficher_zone_saisie(self, lab_nom, zone, bouton):
        lab_nom.pack_forget()  # masquer le label
        zone.pack(pady=10)
        bouton.pack(pady=10)

    def valider_nom(self, nb_j, frame, zone, bouton):
        nom_j = zone.get()
        #Ici, nous regardons quel joueur a saisi le nom pour enregistrer le nom dans notre variable
        #  que nous allons utiliser plus tard.
        if nb_j == 1:
            self.nom_1 = zone.get()
        else:
            self.nom_2= zone.get()
        if nom_j:
            zone.pack_forget()  # masquer la zone de saisie
            bouton.pack_forget()  # masquer le bouton
            label_resultat = tk.Label(frame, text=f"Nom jouer : {nom_j}", font=("Palatino Linotype", 14), bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
            label_resultat.pack(pady=20)
    