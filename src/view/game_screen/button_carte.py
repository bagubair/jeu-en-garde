import os
import tkinter as tk

from consts import LONGUEUR, HAUTEUR, DATA_DIR
from utils.image_size import size_photo

"""
La classe ButtonCarte crée les boutons des cartes.Les cartes que le joueur peut jouer seront activées,
tandis que les autres seront désactivées.Cela est géré par la fonction update_carte,
qui prend les listes de cartes jouées et les possibilités de jeu en paramètre.
Les boutons des cartes sont liés à l'événement pour gérer l'ordre du fonctionnement du jeu.
"""
class ButtonCarte:
    def __init__(self, canvas, jouer_1, jouer_2):
        self.canvas = canvas
        self.lis_possib_jouer = None

        self.nb_move = None

        self.create_butt_carte(self.canvas, jouer_1.cartes)
        self.update_carte(self.canvas, jouer_1.cartes, self.lis_possib_jouer)

    
    def create_butt_carte(self, canvas, cart_possed):
        butt_carte = []
        for i in range(len(cart_possed)):
            # cart_possed[i]  la valeur d'indice i represente la valeur de la carte
            image_carte = size_photo(os.path.join(DATA_DIR, f"carte_{cart_possed[i]}.jpg"), 150, 200)
            carte = cart_possed[i]
            bouton = tk.Button(self.canvas, width=150, height=200, image=image_carte,
                               command=self.click_carte(carte))

            bouton.image = image_carte
            bouton.place(x=(LONGUEUR * .27) + 180 * i, y=(HAUTEUR * .55))
            butt_carte.append(bouton)
        return butt_carte

    def update_carte(self, canvas, cart_possed, possib_joux):
        # on active juste les carte qu'il peux jouer avec
        carte_jouer = self.create_butt_carte(canvas, cart_possed)
        if possib_joux is not None:

            for i in range(len(cart_possed)):
                if cart_possed[i] not in possib_joux:
                    carte_jouer[i].config(state=tk.DISABLED)
        else:
            for carte in carte_jouer :
                carte.config(state=tk.DISABLED)
            

    def click_carte(self, nb_carte):
        def f():
            self.nb_move = nb_carte
            self.callback()

        return f
    def bind(self, callback):
        self.callback = callback

