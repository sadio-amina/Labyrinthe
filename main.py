from labyrinthe import Labyrinthe

# Maze dimensions (ncols, nrows)
n = int(input("Entrez la taille du labyrinthe svp :"))
name = input("Quel nom vous voulez donnez à votre fichier ?")

labie = Labyrinthe(n)

labie.construire_laby()

print(labie)