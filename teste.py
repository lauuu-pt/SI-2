from searchPlus import *
from p2_aux import *

def result(self, state, action): 
        "Tanto as acções como os estados são representados por pares (x,y)."
        (x,y) = state
        (dx,dy) = self.directions[action]
        return (x+dx,y+dy) 
    
def actions(self, state):
        """Podes move-te para uma célula em qualquer das direcções para uma casa 
           que não seja obstáculo."""
        x, y = state
        return [act for act in self.directions.keys() if (x+self.directions[act][0],y+self.directions[act][1]) not in self.obstacles]
    
def line(x, y, dx, dy, length):
    """Uma linha de células de comprimento 'length' começando em (x, y) na direcção (dx, dy)."""
    return {(x + i * dx, y + i * dy) for i in range(length)}

def quadro(x, y, length):
    """Uma moldura quadrada de células de comprimento 'length' começando no topo esquerdo (x, y)."""
    return line(x,y,0,1,length) | line(x+length-1,y,0,1,length) | line(x,y,1,0,length) | line(x,y+length-1,1,0,length)

def manhatan(p,q):
    (x1,y1) = p
    (x2,y2) = q
    return abs(x1-x2) + abs(y1-y2)

def display(pacman,pastilha,obstaculos,path=[]):
    """ print the state please"""
    pacmanX,pacmanY=pacman
    osXs={x for (x,_) in obstaculos | {pastilha, pacman}}
    minX=min(osXs)
    maxX=max(osXs)
    osYs={y for (_,y) in obstaculos | {pastilha, pacman}}
    minY=min(osYs)
    maxY=max(osYs)
    output=""
    for j in range(minY,maxY+1):
        for i in range(minX,maxX+1):
            if pacman ==(i,j):
                ch = '@'
            elif pastilha==(i,j):
                ch = "*"
            elif (i,j) in obstaculos:
                ch = "#"
            elif (i,j) in path:
                ch = '+'
            else:
                ch = "."
            output += ch + " "
        output += "\n"
    print(output)

def graph_search(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    If two paths reach a state, only use the first one. [Figure 3.7]"""
    frontier.append(Node(problem.initial))
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
    return None


def best_first_graph_search(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return node, explored

def rodeia(self,pacman):
    x, y = pacman
    coordenadas = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
    return [coord for coord in coordenadas if coord not in self.obstaculos]

def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))
   


def planeia_online(problem,pacman, pastilha, obstaculos):
        """"
        mundo = {}
    mundo[pastilha] = '*'
    mundo[pacman] = '@'
    direcoes = [(0,1),(0,-1),(1,0),(-1,0)] 
    while True:
        vizinhos = []
        for direcao in direcoes:
            vizinho = tuple(sum(x) for x in zip(pacman, direcao))
            if vizinho not in obstaculos and vizinho not in mundo:
                vizinhos.append(vizinho)
                
        if not vizinhos:
            return None
        
        proximo = min(vizinhos, key=lambda x: abs(x[0]-pastilha[0])+abs(x[1]-pastilha[1]))
        mundo[proximo] = '.'
        pacman = proximo
        
        if pacman == pastilha:
            break 
        """
       
        while pacman!=pastilha:
            """ if pacman == pastilha:
                return None
            else:
                problem = PacmanProblem(pacman, pastilha, obstaculos)
                node = astar_search(problem)
                pacman = node.state
                return node.path() """
            result
            manhatan(pacman,pastilha)
            display(pacman,pastilha,obstaculos,rodeia)
            astar_search(pacman,pastilha,obstaculos=rodeia())
            if pacman == pastilha:
                break 
        
         
pacman=(1,1)
pastilha=(1,6)
l = line(2,2,1,0,6)
c = line(2,3,0,1,4)
fronteira = quadro(0,0,10)
obstaculos=fronteira | l | c
print(planeia_online(pacman,pastilha,obstaculos))




def modelo(pacman, obstaculos):
    modelo = set()
    for xx in [-1, 0, 1]:
        for yy in [-1, 0, 1]:
            for zz in [-1, 0, 1]:
                if (xx != 0 or yy != 0 or zz != 0):
                    x = pacman[0] + xx
                    y = pacman[1] + yy
                    z = pacman[2] + zz
                    if (x >= 0 and y >= 0 and z >= 0):
                        modelo.add((x, y, z))
    obs_modelo = set()
    for pos in modelo:
        if pos in obstaculos:
            obs_modelo.add(pos)
    return obs_modelo