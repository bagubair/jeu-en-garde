import tkinter as tk

from consts import COULEUR_BOUTON , COULEUR_TEXT_BOUTON


class QuitJeu:
    def __init__(self, root, canvas):
        self.root = root
        # ---------------------  Button QuitJeu --------------------------------------
        #Le bouton pour revenir à la page principale.
        self.bot_retour = tk.Button(canvas, width=3, height=1, text="QuitJeu",command=self.click_retour,
                            bg=COULEUR_BOUTON, fg= COULEUR_TEXT_BOUTON, font=("Palatino Linotype", 9, "bold"))
        self.bot_retour.place(relx=0.03, rely=0.03, anchor="center")

    
    def click_retour(self):
        self.root.event_generate("<<retour_clicked>>")

