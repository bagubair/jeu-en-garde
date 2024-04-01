import tkinter as tk

from consts import *
from utils.image_size import size_photo
from view.main_menu.aide_button import Aide
from view.select_screen.retour_button import Retour
from view.select_screen.button_regle import ButtonRegle
from view.select_screen.frame_joueur import FrameJouers
from view.select_screen.frame_plan import FramePlan
from view.select_screen.nom_joueur import NomJouer
from view.jeu_basic import PageJeuBasic 
from view.jeu_classique import PageJeuClassique


# --- Une classe pour intialiser la page de choisir en ajoutant une photo packground et apler les autre classea ----
class ChoixRegle:
    def __init__(self, root):
        self.root = root
        # --------------------- créer un Canvas ----------------------------------------------------
        self.canvas = tk.Canvas(root, width=LONGUEUR, height=HAUTEUR)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        root.grid_rowconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en hauteur
        root.grid_columnconfigure(0, weight=1)  # Poids pour permettre le redimensionnement en largeur

        # ------- apple des classes suivants car dans ces classe on va travalier sur le canvas qu'on a vien de creer
        self.frame_jouer = FrameJouers(self.canvas)
        self.buton_regl = ButtonRegle(self.canvas)
        self.nom_jouer = NomJouer(self.canvas)
        self.frame_plans = FramePlan(self.canvas)
        self.aide = Aide(self.canvas)
        self.retour = Retour(self.root, self.canvas)

        # -------------------- Ajouter l'image au canvas -------------------------------------------
        """
        Charger et redimensionner l'image initiale par appel la fonction size_photo 
        qu'est définit dans modle [utils.image_size.py] ; la fonction prende l'image et les demention en pixle
        """
        self.background_image = size_photo(os.path.join(DATA_DIR, "screen_2.jpg"), LONGUEUR, HAUTEUR)
        self.image_item = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        
        # ----- lier la fonction de redimensionnement à l'événement de changement de taille du canvas
        self.canvas.bind("<Configure>", self.on_canvas_resize)

        """
        Un bouton 'Commencer' pour démarrer le jeu, mais avant cela, le joueur doit choisir la règle,
        la carte sur laquelle il veut jouer et les personnages. 
        Il y a également une option supplémentaire s'il souhaite ajouter des noms pour les joueurs.
        """
        self.bot_continuer = tk.Button(self.canvas, width=8, height=2, text="Commencer", state=tk.DISABLED,
                                       command=self.click_cont,bg=COULEUR_BOUTON, fg=COULEUR_TEXT_BOUTON, 
                                       font=("Palatino Linotype", 12, "bold"))
        self.bot_continuer.place(relx=0.5, rely=0.9, anchor="center")
        self.jour_1 = self.nom_jouer.nom_1
        self.jour_2 = self.nom_jouer.nom_2
        # Metter à jour l'état initial du bouton commencer
        self.update_state()

    # Récupérer la nouvelle taille du canvas
    def on_canvas_resize(self, event):
        new_width = self.canvas.winfo_width()
        new_height = self.canvas.winfo_height()

        # Redimensionner l'image pour s'adapter à la nouvelle taille
        self.background_image = size_photo(os.path.join(DATA_DIR, "screen_2.jpg"), new_width, new_height)
        # Mettre à jour l'image sur le canvas
        self.canvas.itemconfig(self.image_item, image=self.background_image)

    def update_state(self):
        """
        valide resoit la valeur des buttons qui sont obligatoire a choisir pour passer le page de joux 
        si manque un attribue ne peux pas demarer le jeux donc il faut s'assurer les valeurs nesissaire
        """

        valide = (self.buton_regl.regle and self.frame_plans.plan
                  and self.frame_jouer.jouer_1 and self.frame_jouer.jouer_2)
        if valide:
            self.bot_continuer.configure(state=tk.NORMAL)
        else:
            # verifier le changement des valeurs nesissaire apres 200 sec
            self.root.after(200, self.update_state)

    def click_cont(self):
        # Si toutes les valeurs sont définies, imprimez-les ou effectuez d'autres actions nécessaires
        plan = self.frame_plans.plan   # on prend le nombre de plan que les joueur choisi
        nb_phot_1 = self.frame_jouer.jouer_1 # on prend le nombre de photo pour joueur 1 
        nb_phot_2 = self.frame_jouer.jouer_2 # on prend le nombre de photo pour joueur 2
        nom_j_1 = self.nom_jouer.nom_1 # on prnde le nom de joueur 1 que le joueur entree
        nom_j_2 = self.nom_jouer.nom_2 # on prnde le nom de joueur 2 que le joueur entree
        
        if self.buton_regl.regle == 1:
            PageJeuBasic(self.root, plan,nb_phot_1 , nb_phot_2,nom_j_1,nom_j_2)
        elif self.buton_regl.regle == 2 :
            PageJeuClassique(self.root, plan,nb_phot_1 , nb_phot_2,nom_j_1,nom_j_2)



def PageChoix(root):
    choix_page = ChoixRegle(root)
