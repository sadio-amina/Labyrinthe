from labyrinthe import Labyrinthe

# Dimension du labyrinthe et le nom du fichier demandé à l'utilisateur

n = int(input("Entrez la taille du labyrinthe svp :"))
name = input("Quel nom vous voulez donnez à votre fichier ? ")

labie = Labyrinthe(n)
labie.construire_laby()
print(labie)
