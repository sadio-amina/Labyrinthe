# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:04:26 2022

@author: sadio
"""
#n = int(input("Entrez un nombre entier svp: "))

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
    
    def __init__(self, nx, ny, ix=0, iy=0):
        self.nx, self.ny = nx, ny
        self.ix , self.iy = ix, iy
        self.laby_carte = [[Case(x, y) for y in range(ny)] for x in range(nx)]
        print(self.laby_carte) 




case1 = Case(0, 0)
case2 = Case(0, 1)
#print(case1.verifier_murs())
case1.casser_mur('E', case2)
#print(case1.murs)





