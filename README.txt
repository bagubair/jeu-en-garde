En Garde Dragon Ball : Guide Complet du Projet I52 IHM
Fait par : SWAILM Abdullah & BA GUBAIR Emad

Lancement du Jeu
Pour lancer le jeu depuis le terminal, placez-vous dans le répertoire du jeu (src) et exécutez la commande suivante :
python3 ./app.py

Structure du Dossier du Projet
Le dossier du projet est organisé comme suit :

data: Contient toutes les photos et fichiers textes utilisés dans le jeu.
src: Contient l'ensemble des codes du jeu.
app.py: Fichier exécutable du jeu.
consts.py: Contient les valeurs constantes.
cli.py: Code permettant d'exécuter le jeu dans le terminal, prenant en charge les règles basiques.
Dans le répertoire src, vous trouverez également des sous-répertoires regroupant des codes spécifiques :

model: Contient les fichiers "player.py" pour la classe "joueur" et "round.py" pour la classe "round" (tour).
utils: Contient des fonctions utiles telles que "size_image" pour ouvrir et modifier les photos.
view: Contient les codes des règles du jeu, avec une implémentation pour les règles basiques et classiques.
Trois autres dossiers sont présents, chacun regroupant les classes d'une page spécifique :

Page Menu: Boutons "play", "aide" pour consulter les règles, et "quitter" pour fermer l'application.
Page Select: Choix des règles, du plan, et des personnages. La saisie des noms est facultative, mais les autres choix sont obligatoires.
Page Interface du Jeu: Interface du jeu avec les règles, les mouvements, les attaques, et l'affichage des scores.
Déroulement du Jeu


Nous avons abordé uniquement les règles de base et classiques, à l'exception des règles avancées. Notamment, dans le classique, la gestion des situations où la pioche est vide. On examine directement qui a le plus de possibilités d'attaquer, et celui qui gagne, en ignorant si le joueur actuel peut attaquer

Illustrations et Personnages
Les illustrations et les personnages sont inspirés de l'univers de Dragon Ball. Le jeu, intitulé "En Garde Dragon Ball," s'inspire des combats à distance de Dragon Ball. La victoire est déterminée par la remise en jeu de 5 manches.

