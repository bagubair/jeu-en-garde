import tkinter as tk

from consts import COULEUR_BOUTON ,COULEUR_TEXT_BOUTON
"""
La classe Retour permet de créer le bouton de retour pour permettre au joueur de revenir à la page précédente.
"""
class Retour:
    def __init__(self, root, canvas):
        self.root = root

        # ---------------------  Button Retour --------------------------------------
        self.bot_retour = tk.Button(canvas, width=3, height=1, text="Retour",command=self.click_retour,
                         bg=COULEUR_BOUTON, fg=COULEUR_TEXT_BOUTON,font=("Palatino Linotype", 9, "bold"))
        self.bot_retour.place(relx=0.04, rely=0.09, anchor="center")

    # le button Retour pour rerourner a la page precedante
    def click_retour(self):
        self.root.event_generate("<<retour_clicked>>")
