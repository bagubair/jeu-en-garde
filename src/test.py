import os
import tkinter as tk

from model.player import Player
from model.round import Round
from consts import DATA_DIR, LONGUEUR, HAUTEUR, COULEUR_PRINCIPALE
from utils.image_size import size_photo

from view.jeu import RegleBasic

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{LONGUEUR}x{HAUTEUR}")
    root["bg"] = COULEUR_PRINCIPALE
    root.minsize(LONGUEUR, HAUTEUR)
    root.title("En Garde")

    app = RegleBasic(root, 2, 1, 2)
    app.demarer()

    root.mainloop()