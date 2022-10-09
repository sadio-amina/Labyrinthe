# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:04:26 2022

@author: sadio
"""

import random

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
       

    def cell_at(self, x, y): 
        " Retourne l'objet aux coordonnées ( x et y ) "
        return self.laby_carte[x][y]

    def __str__(self):
        """Retourne le format chaine de caractère du labyrinthe ."""

        laby_lignes = ["." +( "#" * self.nx * 2)]
        for y in range(self.ny):
            laby_ligne = ['#']
            for x in range(self.nx):
                if self.laby_carte[x][y].murs['E']:
                    laby_ligne.append('##')
                else:
                    laby_ligne.append('..')
            laby_lignes.append(''.join(laby_ligne))
            laby_ligne = ['#']
            for x in range(self.nx):
                    if self.laby_carte[x][y].murs['S']:
                        laby_ligne.append('##')
                    else:
                        laby_ligne.append('..')
            laby_lignes.append(''.join(laby_ligne))
        return '\n'.join(laby_lignes)



    def chercher_voisins_valide(self, case):
        """Retourne la liste de voisins des cases non visitées ."""

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


    def enregister_fichier(nom_fichier):
        f = open("labyrinthe.txt" , "w")
        lab = f.write(str(labie))
        f.close()
        return lab 



    def lire_fichier(file_name):
        nv_laby = []
        f = open("labyrinthe.txt")
        labyrinthe = f.read()
        f.close()
        labth = labyrinthe.splitlines()
        for ligne in labth:
            nv_laby.append(list(ligne))

        print(nv_laby)



#labie = Labyrinthe(10)
#labie.construire_laby()
#print(labie)
#labie.enregister_fichier()
# labie.lire_fichier()















