# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:04:26 2022

@author: sadio
"""

import random
#n = int(input("Entrez un nombre entier svp: ")) (dans le fichier main)

class Case :
    """ Les cellules sont entourées par les murs à
    l'Ouest, l'Est, le Nord et le Sud

    """

    paires_murs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """ Les cellulles ont des coordonnées x et y selon les murs"""
        self.x = x
        self.y = y
        self.murs = { 'N': True, 'S': True, 'W':True, 'E': True}

    def verifier_murs(self):
        """ Vérifier si tous les murs sont en places """
        return self.murs.values()

    def casser_mur(self, mur, autre):
        """ Casser les murs entre les cellulles """
        self.murs[mur] = False
        autre.murs[Case.paires_murs[mur]] = False



class Labyrinthe:
    "Modélisation du labyrinthe partant des cellules et de leurs indexes i et j"
    
    def __init__(self, n, ix=0, iy=0):
        self.nx, self.ny = n, n
        self.ix , self.iy = ix, iy
        self.laby_carte = [[Case(x, y) for y in range(n)] for x in range(n)]
       
        # for x in range(nx):
        #     for y in range((ny)):
        #         print(x,y)
        

    def cell_at(self, x, y): 
         return self.laby_carte[x][y]

    def __str__(self):
        """Return a (crude) string representation of the maze."""

        laby_lignes = ["." +( "#" * self.nx * 2)]
        for y in range(self.ny):
            laby_ligne = ['# ']
            for x in range(self.nx):
                if self.laby_carte[x][y].murs['E']:
                    laby_ligne.append('# ')
                else:
                    laby_ligne.append('. ')
            laby_lignes.append(''.join(laby_ligne))
            laby_ligne = ['# ']
            for x in range(self.nx):
                    if self.laby_carte[x][y].murs['S']:
                        laby_ligne.append('# ')
                    else:
                        laby_ligne.append('. ')
            laby_lignes.append(''.join(laby_ligne))
        return '\n'.join(laby_lignes)

    def chercher_voisins_valide(self, case):
        """Retourne la liste de voinsins des cases non visitées ."""

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        voisins = []
        for direction, (dx, dy) in delta:
            x2, y2 = case.x + dx, case.y + dy
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):
                 voisin = self.cell_at(x2, y2)
                 if voisin.verifier_murs():
                    voisins.append((direction, voisin))

                     
        return voisins

    def construire_laby(self):
        # Nombre total de cases.
        n = self.nx * self.ny
        case_empile = []
        case_courante = self.cell_at(self.ix, self.iy)
        
        # nombre de case visité de base 
        nv = 1

        while nv < n:
           voisins= self.chercher_voisins_valide(case_courante)
           if not voisins:
                case_courante = case_empile.pop()
                
                continue

           direction, next_cell = random.choice(voisins)
           case_courante.casser_mur(autre=next_cell, mur=direction)
           case_empile.append(case_courante)
           case_courante = next_cell
           nv += 1

        

      

labie = Labyrinthe(5)
labie.construire_laby()
#print(labie)
labie= str(labie)

def enregister_fichier(nom_fichier):
    f = open(nom_fichier , "w")
    labyrint = f.write(labie)
    f.close()
    return labyrint

enregister_fichier("labyrinthe.txt")
def lire_fichier(file_name):
    f = open(file_name)
    maze = f.read()
    f.close()
    return maze

lire_fichier("labyrinthe.txt")


# def convert_maze(maze):
#     converted_maze = []
#     lines = maze.splitlines()
#     for line in lines:
#         converted_maze.append(list(line))
#     return converted_maze



case1 = Case(0, 0)
#case2 = Case(0, 1)

#print(case1.verifier_murs())
case1.casser_mur('E', case1)
#print(case1.murs)





