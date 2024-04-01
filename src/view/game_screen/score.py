import os
import tkinter as tk

from consts import DATA_DIR , COULEUR_TEXT_BOUTON , COULEUR_BOUTON
from utils.image_size import size_photo
"""
Classe Score pour ajouter la photo identificateur du joueur dans les coins de la fenêtre
et afficher leurs noms et scores.Cette classe contient également une fonction update pour
mettre à jour le score.
"""

class Score:
    def __init__(self, canvas,tour):
        # Créez les widget image pour les photo identificateur des jours
        self.photo_jouer_1 = size_photo(os.path.join(DATA_DIR, f"jouer_{tour.players[0].photo}.png"), 150, 170)
        self.widg_image_1 = canvas.create_image(40, 150, anchor=tk.W, image=self.photo_jouer_1)

        self.photo_jouer_2 = size_photo(os.path.join(DATA_DIR, f"jouer_{tour.players[1].photo}.png"), 150, 170)
        self.widg_image_2 = canvas.create_image(1885, 150, anchor=tk.E, image=self.photo_jouer_2)

        # Ajoutez des labels a cote de l'image
        #------ label nom joueur 
        self.nom_label_1 = tk.Label(canvas, text=tour.players[0].nom, padx=10, pady=10, font=("Palatino Linotype", 13, "bold"),
                                    bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.nom_label_1.place(relx=0.098, rely=0.095, anchor=tk.W)  
        self.nom_label_2 = tk.Label(canvas, text=tour.players[1].nom, padx=10, pady=10, font=("Palatino Linotype", 13, "bold"),
                                    bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.nom_label_2.place(relx=0.905, rely=0.095, anchor=tk.E)  
        #------ label score joueur
        self.label_scor_1 = tk.Label(canvas, text="Score", padx=10, pady=10, font=("Palatino Linotype", 13, "bold"),
                                    bg=COULEUR_BOUTON, fg=COULEUR_TEXT_BOUTON)
        self.label_scor_1.place(relx=0.098, rely=0.13, anchor=tk.W)  
        self.label_scor_2 = tk.Label(canvas, text="Score", padx=10, pady=10, font=("Palatino Linotype", 13, "bold"),
                                    bg=COULEUR_BOUTON, fg=COULEUR_TEXT_BOUTON)
        self.label_scor_2.place(relx=0.905, rely=0.13, anchor=tk.E)  
        #------ label score joueur
        self.scor_zone_1 = tk.Label(canvas, text=tour.players[0].score, padx=10, pady=10, font=("Palatino Linotype", 16, "bold"),
                                    bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.scor_zone_1.place(relx=0.098, rely=0.177, anchor=tk.W)  
        self.scor_zone_2 = tk.Label(canvas, text=tour.players[1].score, padx=10, pady=10, font=("Palatino Linotype", 16, "bold"),
                                    bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.scor_zone_2.place(relx=0.905, rely=0.177, anchor=tk.E)


    def update_score(self, tour):
        self.scor_zone_1.config(text=tour.players[0].score)
        self.scor_zone_2.config(text=tour.players[1].score)

    