from searchPlus import *
from p2_aux import *

def result(self, state, action): 
        "Tanto as acções como os estados são representados por pares (x,y). from PL"
        (x,y) = state
        (dx,dy) = self.directions[action]
        return (x+dx,y+dy)
    
def actions(self, state):
        """Podes move-te para uma célula em qualquer das direcções para uma casa 
           que não seja obstáculo. from PL"""
        x, y = state
        return [act for act in self.directions.keys() if (x+self.directions[act][0],y+self.directions[act][1]) not in self.obstacles]
 
pacman=(1,1)
pastilha=(1,6)
l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10)
obstaculos=fronteira | l | c   
print(display(pacman=(1,1),pastilha=(1,6),obstaculos=fronteira | l | c ,path=[]))
def planeia_online(pacman, pastilha, obstaculos):
    self.pacman=pacman
    self.pastilha=pastilha
    self.obstaculos=obstaculos
    pass
def __init__(self, initial = ((1,1),0), goal=1, pastilhas={}, obstacles=quadro(0,0,10), dim=10):
        self.initial = initial
        self.pacman = initial[0] # (x,y) que representa a posição inicial do Pacman
        self.pontos = initial[1]
        self.goal = goal # o nº mínimo de pontos que o Pacman deve obter
        self.pastilhas = pastilhas # conjunto das pastilhas: dicionário com chaves {N,D,C} e os valores são uma lista de tuplos correspondentes às posições das pastilhas
        self.obstacles = obstacles # conjunto de obstáculos
        self.dim = dim # dimensão do mundo

