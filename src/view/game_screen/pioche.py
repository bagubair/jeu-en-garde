import os
import tkinter as tk

from consts import DATA_DIR , COULEUR_BOUTON , COULEUR_TEXT_BOUTON
from utils.image_size import size_photo
"""
La classe Pioche sert uniquement à afficher une image de carte cachée tant qu'il y a des cartes dans la liste 'paquet_pioche'.
Cela montre qu'il y a encore des cartes à jouer. Lorsque la liste est vide, l'image disparaît.
De plus, la classe contient le widget image pour afficher la dernière carte jouée. Au départ,
il n'y a pas d'image jusqu'au démarrage du jeu.
"""
class Pioche:
    def __init__(self, canvas, tour):
        self.canv = canvas
        self.widg_pioche = None 
        self.photo_pioche = None # Buffer pour stocker l'image et la sauvegarder après l'avoir modifiée par la fonction size_photo
        self.lab_pioch = tk.Label(self.canv, text="Pioche", padx=10, pady=4, font=("Palatino Linotype", 18, "bold"),
                                    bg=COULEUR_BOUTON ,fg=COULEUR_TEXT_BOUTON)
        self.lab_pioch.place(relx=0.055, rely=0.59, anchor=tk.W)
        self.lab_used = tk.Label(self.canv, text="Carte Utiliseé", padx=10, pady=8, font=("Palatino Linotype", 10, "bold"),
                                bg=COULEUR_BOUTON ,fg=COULEUR_TEXT_BOUTON)
        self.lab_used.place(relx=0.87, rely=0.59, anchor=tk.W)

        self.widg_utilise = None
        self.photo_utilise = None  # Buffer pour stocker l'image et la sauvegarder après l'avoir modifiée par la fonction size_photo
        self.lab_used = None

        self.intialse_pioche(tour.paquet_pioche)

    def intialse_pioche(self,list_pioche):
        self.carte_pioche(list_pioche)
        self.carte_used()

    def carte_pioche(self, list_pioche):
        if len(list_pioche) != 0:
            self.photo_pioche = size_photo(os.path.join(DATA_DIR, "pioche.jpg"), 150, 230)
            self.widg_pioche = self.canv.create_image(100, 700, anchor=tk.W, image=self.photo_pioche)
            self.lab_pioch = tk.Label(self.canv, text=f"Cartes restes : {len(list_pioche)}", padx=10, pady=4, 
                                    font=("Palatino Linotype", 10, "bold"),bg=COULEUR_BOUTON ,fg=COULEUR_TEXT_BOUTON)
            self.lab_pioch.place(relx=0.047, rely=0.87, anchor=tk.W)
        else:
            self.canv.delete(self.widg_pioche)

    def carte_used(self, nb=0):
        if nb != 0:
            self.photo_utilise = size_photo(os.path.join(DATA_DIR, f"carte_{nb}.jpg"), 150, 230)
            self.widg_utilise = self.canv.create_image(1670, 700, anchor=tk.W, image=self.photo_utilise)
            
        else:
            self.canv.delete(self.widg_utilise)


    