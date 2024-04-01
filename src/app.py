# app.py
import tkinter as tk

from consts import *
from view.select_screen.choix_regle import PageChoix
from view.main_menu.background import BackGroundMain


class RootPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{LONGUEUR}x{HAUTEUR}")
        self.root["bg"] = COULEUR_PRINCIPALE
        self.root.minsize(LONGUEUR, HAUTEUR)
        self.root.title("En Garde")
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.main_screen()

    def main_screen(self):
        BackGroundMain(self.root)
        bouton = tk.Button(self.root, text="Play", width=25, height=2, command=self.click_play, bg=COULEUR_BOUTON,
                            fg=COULEUR_TEXT_BOUTON,font=("Georgia", 15, "bold"))

        bouton.place(relx=0.5, rely=0.93, anchor="center")

        self.root.bind("<<retour_clicked>>", self.click_retour)

    def click_play(self):
        self.root.event_generate("<<play_clicked>>")
        PageChoix(self.root)

    def click_retour(self, event=None):
        self.main_screen()

    def mainloop(self):
        self.root.mainloop()


# "Comic Sans MS", 18, "italic" ou bold   pour mot EN GARDE
def Demarer():
    app = RootPrincipal()
    app.mainloop()


if __name__ == "__main__":
    Demarer()
