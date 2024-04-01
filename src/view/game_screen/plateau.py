import os.path
import tkinter as tk

from consts import DATA_DIR
from utils.image_size import size_photo

"""
La classe Plateau gère la création du canvas du plateau pour les cases du jeu.
Elle contient également la fonction 'file_case' pour placer une photo sur la case,
et la fonction 'initialiser_case' pour initialiser les places des joueurs au début du tour.
La fonction 'move_joueur' récupère le mouvement du joueur selon sa nouvelle position
"""

class Plateau:
    def __init__(self, canvas, jouer_1, jouer_2, linge=1, col=23):
        self.canvas = canvas
        self.cols = col
        self.linges = linge

        self.canvas_plat = tk.Canvas(self.canvas, width=self.cols * 40, height=100, bg="white")
        self.canvas_plat.place(relx=0.0, rely=0.42, anchor=tk.W)

        self.list_rect = self.create_pist()
        self.photos = {}

        self.canvas_plat.bind("<Configure>", self.on_canvas_resize)

    def create_pist(self):
        # Créer une fenêtre avec un plateau de 23 case
        l = []
        for col in range(self.cols):
            l.append(self.create_case(col))

        return l

    def create_case(self, cols):
        # Calcule les coordonnées de la case
        x1, y1 = cols * 60, 0
        x2, y2 = (cols + 1) * 60, 60

        # Crée un rectangle représentant la case
        return self.canvas_plat.create_rectangle(x1, y1, x2, y2, outline="black")

    def file_case(self, col, photo, nb_tag):
        # Place l'image dans la case de plateux
        x = (col * 83 + (col + 1) * 83) // 2
        y = 90

        photo = size_photo(photo, 45, 170)
        self.canvas_plat.create_image(x, y, image=photo, tags=f"tag_image_{nb_tag}")
        return photo

    def intiale_case(self, j1, j2):
        self.photos[j1.id] = self.file_case(j1.position, os.path.join(DATA_DIR, f"jouer_{j1.photo}.png") , j1.id)
        self.photos[j2.id] = self.file_case(j2.position, os.path.join(DATA_DIR, f"jouer_{j2.photo}.png") , j2.id)
        
    def move_joueur(self, joueur):
        photo = os.path.join(DATA_DIR, f"jouer_{joueur.photo}.png")
        self.canvas_plat.delete(self.photos[joueur.id])
        self.photos[joueur.id] = self.file_case(joueur.position, photo , joueur.id)
        
    def on_canvas_resize(self, event):
        # Récupérer la nouvelle taille du canvas
        new_width = self.canvas.winfo_width()
        new_height = self.canvas.winfo_height()

        self.canvas_plat.config(width=new_width, height=new_height / 6)

        # Mettre à jour la taille et la position des rectangles sur le canevas
        for i in range(self.cols):
            co = i
            x1, y1 = co * new_width / self.cols, 0
            x2, y2 = (co + 1) * new_width / self.cols, new_height
            self.canvas_plat.coords(self.list_rect[i], x1, y1, x2, y2)
