import tkinter as tk

from consts import COULEUR_BOUTON, COULEUR_TEXT_BOUTON ,LONGUEUR, HAUTEUR
"""
La classe ChoixMove permet de choisir le type de mouvement que le joueur souhaite effectuer.
"""

class ChoixMove:
    def __init__(self, canvas):
        self.canv = canvas
        self.type_move = ["Avancer", "Reculer", "Attaquer"]
        self.boutons = []
        self.type = None  # Sauvegarder le type de mouvement ; on le teste après en effectuant le mouvement.
        self.callback = None

        # Création des boutons ["Avancer", "Reculer", "Attaquer"] sur le canvas
        for i, text in enumerate(self.type_move):
            bouton = tk.Button(self.canv, text=text, width=7, height=2, command=self.choix_type(i),
                               bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON,  font=("Palatino Linotype", 13, "bold"))
            bouton.place(x=(LONGUEUR * .38) + 180 * i, y=(HAUTEUR * .8))
            self.boutons.append(bouton)

    def choix_type(self, number):
        def f():
            self.type = number +1
            self.callback()
        return f

    def bind(self, callback):
        self.callback = callback
