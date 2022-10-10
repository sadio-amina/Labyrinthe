import png, numpy, Queue, operator, itertools ,random


print("ne me donne que des nombre entier sinon ça ne va pas le faire")

n = int(input("t'on nombre ?"))

direction_Random = random.choice(['N','S','W','E'])
numero_Random = random.randrange(1,n)



class Case :
    """
    Les cellules sont entourées par les murs à
    l'Ouest, l'Est, le Nord et le Sud
    """
    paires_murs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    chiffre_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
    
    def __init__(self, x, y):
        """ Les cellulles ont des coordonnées x et y selon les murs"""
        self.x = x
        self.y = y
        self.number = None
        self.murs = { 'N': True, 'S': True, 'W':True, 'E': True}
        
    def verifier_numbers(self):
        """ Vérifier si le nombre de reconaisence est bien la """
        return self.number.values()
    
    def verifier_murs(self):
        """ Vérifier si tous les murs sont en places """
        return self.murs.values()

    def casser_murs(self, mur, autre):
        """ Casser les murs entre les cellulles """
        self.murs[mur] = False
        autre.murs[Case.paires_murs[mur]] = False
        
    def fusion_number(self, number, autre):
        """additionne deux chiffre entre eux"""
        if Case != number:
            # number=>number
            number <= number
        
class Labyrinthe:
    "Modélisation du labyrinthe partant des cellules et de leurs indexes i et j"""
    
    def __init__(self, nx, ny, ix=0, iy=0):
        self.nx , self.ny = nx, ny
        self.ix , self.iy = ix, iy
        self.laby_carte = [[Case(x ,y)for y in range(ny)] for x in range(nx)]
        print(self.laby_carte)
        


case_li = list()

#print(case1.verifier_murs())
# case1.casser_mur('E', case2)
#print(case1.murs)

    #debut de l'algorithme de kruskal 

    #reconaissence du mur
def Algo_laby(Case):
    labyrinthe_de_kruskal=[[Case(x, y)for x in range(n)]for y in range(n)]
    for ligne in labyrinthe_de_kruskal :
        for case in ligne:
            case.number ==numero_Random
            case.casser_murs(direction_Random, case)
            print(case)

def is_white(coord, image):
  """ Returns whether (x, y) is approx. a white pixel."""
  a = True
  for i in xrange(3):
    if not a: break
    a = image[coord[1]][coord[0] * 3 + i] > 240
  return a

def bfs(s, e, i, visited):
  """ Perform a breadth-first search. """
  frontier = Queue.Queue()
  while s != e:
    for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
      np = Tuple(map(operator.add, s, d))
      if is_white(np, i) and np not in visited:
        frontier.put(np)
    visited.append(s)
    s = frontier.get()
  return visited

def main():
  r = png.Reader(filename = "thescope-134.png")
  rows, cols, pixels, meta = r.asDirect()
  assert meta['planes'] == 3 # ensure the file is RGB
  image2d = numpy.vstack(itertools.imap(numpy.uint8, pixels))
  start, end = (402, 985), (398, 27)
  print bfs(start, end, image2d, [])