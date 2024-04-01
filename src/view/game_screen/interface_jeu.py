import os
import tkinter as tk

from model.player import Player
from model.round import Round
from consts import DATA_DIR, LONGUEUR, HAUTEUR, COULEUR_PRINCIPALE
from utils.image_size import size_photo
from view.game_screen.pioche import Pioche
from view.game_screen.button_carte import ButtonCarte
from view.game_screen.choix_move import ChoixMove
from view.game_screen.plateau import Plateau
from view.game_screen.score import Score
from view.game_screen.quit_jeu import QuitJeu

"""
La classe InterfaceJeu sert à initialiser l'interface du jeu en appelant toutes les classes nécessaires.
"""
class InterfaceJeu:
    def __init__(self, root, plan, jouer_1, jouer_2, tour):
        self.root = root
        self.tour = tour
        self.plan = os.path.join(DATA_DIR, f"packG_{plan}.jpg")
        self.photo_1 = os.path.join(DATA_DIR, f"jouer_{jouer_1.photo}.png")
        self.photo_2 = os.path.join(DATA_DIR, f"jouer_{jouer_2.photo}.png")
        # --------------------- créer un Canvas ----------------------------------------------------
        self.canvas = tk.Canvas(self.root, width=LONGUEUR, height=HAUTEUR)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en hauteur
        self.root.grid_columnconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en largeur

        # --------------------- Charger et redimensionner l'image initiale  ------------------------
        self.background_image = size_photo(self.plan, LONGUEUR, HAUTEUR)

        # -------------------- Ajouter l'image au canvas -------------------------------------------
        self.image_item = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # ----- lier la fonction de redimensionnement à l'événement de changement de taille du canvas
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        # ----------------- Appele des classes quon va utiliser sur l'interface du jeu -----------------
        self.score = Score(self.canvas, tour)
        self.plateau = Plateau(self.canvas, jouer_1, jouer_2)
        self.bouton_carte = ButtonCarte(self.canvas, jouer_1, jouer_2)
        self.pioche = Pioche(self.canvas, tour)
        self.choix_move = ChoixMove(self.canvas)
        self.quit_jeu = QuitJeu(self.root, self.canvas)


    # La fonction pour réinitialiser l'interface à chaque nouveau jeu. 
    def reintailise_interface(self,canvas, tour) :
        self.plateau = Plateau(canvas, tour.players[0], tour.players[1])
        self.pioche = Pioche(self.canvas,tour)


    # Récupérer la nouvelle taille du canvas
    def on_canvas_resize(self, event):
        new_width = self.canvas.winfo_width()
        new_height = self.canvas.winfo_height()

        # Redimensionner l'image pour s'adapter à la nouvelle taille
        self.photo = size_photo(self.plan, new_width, new_height)
        # Mettre à jour l'image sur le canvas
        self.canvas.itemconfig(self.image_item, image=self.photo)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{LONGUEUR}x{HAUTEUR}")
    root["bg"] = COULEUR_PRINCIPALE
    root.minsize(LONGUEUR, HAUTEUR)
    root.title("En Garde")

    jouer_1 = Player("Emad ", 1)
    jouer_2 = Player("Emad ", 2)
    tour = Round([jouer_1, jouer_2])
    interface = InterfaceJeu(root, 2, jouer_1, jouer_2, tour)
    root.mainloop()
