import tkinter as tk
from tkinter import messagebox
from consts import COULEUR_BOUTON , COULEUR_TEXT_BOUTON

"""
La classe ButtonRegle pour construire les boutons de choix du niveau de jeu.
por le niveau avancer c'est pas encore disponible donc va afficher message d'erruer 
lorsque le joueur choisi ce niveau
"""
class ButtonRegle:
    def __init__(self, canvas):
        self.bou_text = ["Basic", "Classique", "Avancer"]
        self.boutons = []
        self.regle = tk.IntVar()  # Sauvegarder la règle qui a été choisie pour la récupérer plus tard dans la page suivante.
        self.create_boutons(canvas)

    def create_boutons(self, canvas):
        # Création des boutons [Base, Classique, Avancer] sur le canvas
        for i, text in enumerate(self.bou_text):
            bouton = tk.Button(canvas, text=text, width=7, height=2, command=self.click_regle(i + 1),
                        bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON, font=("Palatino Linotype", 12, "bold"))
            bouton.place(relx=(i + 1) * 0.25, rely=0.25, anchor="center")
            self.boutons.append(bouton)

    def click_regle(self, number):
        def f():
            if number == 3:
                messagebox.showerror("Erreur","Oops,Le niveau avancer n'est pas encore disponible ; choisissez un autre niveau.")
            else:
                self.regle = number
        return f
