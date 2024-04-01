import sys
import tkinter as tk

from consts import COULEUR_BOUTON ,COULEUR_TEXT_BOUTON


class Quitter:
    def __init__(self, canvas):
        quit_button = tk.Button(canvas, text="Quitter", width=5, height=1, font=("Palatino Linotype", 10),
                    bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON, command=self.confirmer_quitter)
        quit_button.place(relx=0.04, rely=0.09, anchor="center")

    def confirmer_quitter(self):
        reponse = tk.messagebox.askquestion("Confirmation", "Êtes-vous sûr de vouloir quitter?")
        if reponse == 'yes':
            sys.exit()
