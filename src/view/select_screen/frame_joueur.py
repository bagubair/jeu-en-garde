import os
import tkinter as tk

from consts import DATA_DIR , COULEUR_BOUTON,COULEUR_TEXT_BOUTON
from utils.image_size import size_photo

"""
La classe FrameJouers pour construire un cadre où nous placerons des photos des personnages du jeu.
Chaque joueur doit choisir le personnage qu'il souhaite ( c'est obligatoire)
Donc, nous avons deux cadres(frame). Dans chaque cadre, nous avons un canevas (pour gérer la barre de défilement [Scrollbar]).
Et dans le canevas, nous avons un autre cadre pour placer les boutons des personnages.
"""
class FrameJouers:
    def __init__(self, canvas):
        # ----------------------------- POUR JOUER 1 ----------------------------------------
        # --------------------- définir un frame pour mettre le nouveux canvas sur ---------
        self.frame_jouers_1 = tk.Frame(canvas, width=300, height=300, bg=COULEUR_BOUTON )
        self.frame_jouers_1.place(relx=0.15, rely=0.75, anchor="center")
        # --------------------- cree un canvas avec le Scrollbar ---------------------------
        self.canv_jouers_1 = tk.Canvas(self.frame_jouers_1, width=300, height=300, yscrollincrement=8 ,bg=COULEUR_BOUTON)
        self.scrol_jouers_1 = tk.Scrollbar(self.frame_jouers_1, command=self.canv_jouers_1.yview, orient="vertical" , bg=COULEUR_BOUTON)
        self.scrol_jouers_1.pack(side="right", fill="y")
        self.canv_jouers_1.configure(yscrollcommand=self.scrol_jouers_1.set)
        self.canv_jouers_1.pack()
        # --------------------- ajoute un Label dans frame extern( frame_jouer_1 ) ---------
        self.titre_jouers_1 = tk.Label(self.frame_jouers_1, text="choisissez un personage 1",font=("Palatino Linotype", 12, "bold"),
                                        bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.titre_jouers_1.pack(side="bottom")
        # --------- cree un frame dans le canvas intern pour placer les bouton dans --------
        self.inner_frame_jouers_1 = tk.Frame(self.canv_jouers_1 ,width=300, height=300, bg=COULEUR_BOUTON)
        self.canv_jouers_1.create_window((0, 0), window=self.inner_frame_jouers_1, anchor='nw')

        # ------------------------------- POUR JOUER 2 --------------------------------------
        # -------------------- définir un frame pour mettre le nouveux canvas sur ----------
        self.frame_jouers_2 = tk.Frame(canvas, width=300, height=300 ,bg=COULEUR_BOUTON)
        self.frame_jouers_2.place(relx=0.85, rely=0.75, anchor="center")
        # -------------------- cree un canvas avec le Scrollbar ----------------------------
        self.canv_jouers_2 = tk.Canvas(self.frame_jouers_2, width=300, height=300, yscrollincrement=8 ,bg=COULEUR_BOUTON)
        self.scrol_jouers_2 = tk.Scrollbar(self.frame_jouers_2, command=self.canv_jouers_2.yview, orient="vertical" , bg=COULEUR_BOUTON)
        self.scrol_jouers_2.pack(side="right", fill="y")
        self.canv_jouers_2.configure(yscrollcommand=self.scrol_jouers_2.set)
        self.canv_jouers_2.pack()
        # --------------------- ajoute un Label en frame extern( frame_jouers_2 ) ----------
        self.titre_jouers_2 = tk.Label(self.frame_jouers_2, text="choisissez un personage 2",font=("Palatino Linotype", 12, "bold"),
                                bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.titre_jouers_2.pack(side="bottom")
        # ---------- cree un frame dans le canvas intern pour placer les bouton dans -------
        self.inner_frame_jouers_2 = tk.Frame(self.canv_jouers_2 ,width=300, height=300, bg=COULEUR_BOUTON)
        self.canv_jouers_2.create_window((0, 0), window=self.inner_frame_jouers_2, anchor='nw')

        # ------------- variable pour sauvgarder les personages choisi par les jouers ------
        self.jouer_1 = tk.IntVar()
        self.jouer_2 = tk.IntVar()

        self.ref_photo = []  # conserve une référence à chaque photo
        self.choix_jouer()

    def choix_jouer(self):
        boutons_jouer_1 = []
        boutons_jouer_2 = []
        for i in range(3):
            for j in range(2):
                # Charger l'images pour des boutons
                image_path = os.path.join(DATA_DIR, f"jouer_{(i * 2) + j + 1}.png")
                # on modifie les demention de photo pour ce soit sur le bouton
                image_modf = size_photo(image_path, 140, 200)
                # on ajoute le photo modifier dans la liste pour faire un reference de la photo
                self.ref_photo.append(image_modf)

                # --------------------- Jouer 1 --------------------------------
                bouton_jouer_1 = tk.Button(self.inner_frame_jouers_1, command=self.click_jouet_1((i * 2)+j+1),
                                           bd=0, compound=tk.TOP)
                bouton_jouer_1.config(width=140, height=200, image=image_modf)
                boutons_jouer_1.append(bouton_jouer_1)
                bouton_jouer_1.grid(row=i, column=j, padx=3, pady=3)
                # --------------------- Jouer 2 --------------------------------
                bouton_jouer_2 = tk.Button(self.inner_frame_jouers_2, command=self.click_jouet_2((i * 2)+j+1),
                                           bd=0)
                bouton_jouer_2.config(width=140, height=200, image=image_modf)
                bouton_jouer_2.grid(row=i, column=j, padx=3, pady=3)
                boutons_jouer_2.append(bouton_jouer_2)

        # Ajustez la hauteur de la inner_frame en fonction du nombre total de boutons
        self.inner_frame_jouers_1.update_idletasks()  # --------- JOUER 1
        self.canv_jouers_1.configure(scrollregion=self.canv_jouers_1.bbox("all"))

        self.inner_frame_jouers_2.update_idletasks()  # --------- JOUER 2
        self.canv_jouers_2.configure(scrollregion=self.canv_jouers_2.bbox("all"))

    def click_jouet_1(self, number):
        def f():
            self.jouer_1 = number
        return f

    def click_jouet_2(self, number):
        def f():
            self.jouer_2 = number
        return f
