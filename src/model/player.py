class Player:
    def __init__(self, nom, nb_photo=None, num=0):
        self.id = num
        self.nom = nom
        self.photo = nb_photo
        self.position = 0
        self.score = 0
        self.cartes = []
        self.avance_possible = []
        self.attaque_possible = []
        self.retour_possible = []

    def avancer(self, nb_cases):
        self.position += nb_cases

    def possibilities(self):
        return len(self.avance_possible) or len(self.attaque_possible) or len(self.retour_possible)
