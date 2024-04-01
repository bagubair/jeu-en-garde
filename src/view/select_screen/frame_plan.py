import os
import tkinter as tk

from consts import DATA_DIR , COULEUR_BOUTON,COULEUR_TEXT_BOUTON
from utils.image_size import size_photo

"""
La classe FramePlan pour construire un cadre(frame) où nous placerons des plans du jeu.
il faut choisir un plan pour jouer sur( c'est obligatoire)
"""
class FramePlan:
    def __init__(self, canvas):
        # --------- définir un frame pour mettre le nouveux canvas dans -------
        self.frame_plan = tk.Frame(canvas, width=400, height=300 , bg=COULEUR_BOUTON)
        self.frame_plan.place(relx=0.5, rely=0.6, anchor="center")
        # -------------------- cree un canvas & Scrollbar ---------------------
        self.canv_plan = tk.Canvas(self.frame_plan, width=400, height=300, yscrollincrement=8 , bg=COULEUR_BOUTON)
        self.scrol = tk.Scrollbar(self.frame_plan, command=self.canv_plan.yview, orient="vertical" , bg=COULEUR_BOUTON )
        self.scrol.pack(side="right", fill="y")
        self.canv_plan.configure(yscrollcommand=self.scrol.set)
        self.canv_plan.pack()
        # ------------------- ajoute un Label dans le frame extern( plan ) --------
        self.titre_plan = tk.Label(self.frame_plan, text="choisissez une carte", font=("Palatino Linotype", 12, "bold"),
                            bg=COULEUR_BOUTON,fg=COULEUR_TEXT_BOUTON)
        self.titre_plan.pack(side="bottom")
        # ----- cree un frame dans le canvas intern pour placer les bouton dans --------
        self.inner_frame = tk.Frame(self.canv_plan , width=400, height=300 , bg=COULEUR_BOUTON)
        self.canv_plan.create_window((0, 0), window=self.inner_frame, anchor='nw')

        self.plan = tk.IntVar()  # ----- variable pour stocker le plan choisi ---------
        self.ref_plan = []
        self.choix_plan()

    def choix_plan(self):
        for i in range(4):

            image_modf = size_photo(os.path.join(DATA_DIR, f"packG_{i + 1}.jpg"), 400, 200)
            # on ajoute le photo modifier dans la liste pour faire un reference de la photo
            self.ref_plan.append(image_modf)

            bouton = tk.Button(self.inner_frame, command=self.clique_plan(i + 1), bd=0)
            bouton.config(width=400, height=200, image=image_modf)
            bouton.pack(padx=3, pady=3)

        # Ajustez la hauteur de la inner_frame en fonction du nombre total de boutons
        self.inner_frame.update_idletasks()
        self.canv_plan.configure(scrollregion=self.canv_plan.bbox("all"))

    def clique_plan(self, number):
        def f():
            self.plan = number
        return f
