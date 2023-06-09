from searchPlus import *
from p2_aux import *


class GridProblem(Problem):
    """Encontrar um caminho numa grelha 2D com obstáculos. Os obstáculos são células (x, y)."""

    def __init__(self, initial=(1, 1), goal=(7, 8), obstacles=()):
        self.initial=initial
        self.goal=goal 
        self.obstacles=set(obstacles) - {initial, goal}

    directions = {"N":(0, -1), "W":(-1, 0), "E":(1,  0),"S":(0, +1)}  # ortogonais
    
                  
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
        
    def manhatan_goal(self,no) : 
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        return manhatan(no.state,self.goal)
    


def mais_melhor_bom_procura_graph(problem, f):
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
            return node, explored
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return node

def a_estrelita(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return mais_melhor_bom_procura_graph(problem, lambda n: n.path_cost + h(n))


def modelo(pacman, obstaculos):
    modelo = []
    for xx in [-1, 0, 1]:
            for yy in [-1, 0, 1]:
                
                if (xx != 0 or yy != 0 ):
                    x = pacman[0] + xx
                    y = pacman[1] + yy
                       
                    if (x >= 0 and y >= 0 ):
                        if (x,y) in obstaculos:
                            modelo.append((x, y))
    
    return modelo
    
    



def planeia_online(pacman, pastilha, obstaculos):
    print('MUNDO')
    display(pacman,pastilha,obstaculos)
    print('MODELO')
        
    es = modelo(pacman,obstaculos) #estado inicial
    display(pacman,pastilha,set(es))
    listaes = es

    espacos_espandidos = 0
    nr_iteracoes = 1

        

    pacA = pacman

    while pastilha != pacA:
            
                #copiar grid problem
                #g= grid....
            caminho = []
            Problemo = GridProblem(pacA, pastilha, listaes)
            estrela_start, explorado = a_estrelita(Problemo, Problemo.manhatan_goal)
            
            for pac in estrela_start.path():
                pac1 = pac.state

                if not pac1  in obstaculos:
                    #adicionar pacman
                    pacA=pac1
                    #adicionar Path
                    caminho.append(pac.state)
                    listaes +=(modelo(pacA,obstaculos))
                    #procurar diferenca de extend
                   
                                
                else:
                    break

            print("ITERAÇÃO: " + str(nr_iteracoes))
            nr_iteracoes += 1
            print(estrela_start.solution())
            print("Expandidos " + str(len(explorado)))
            #print(listaes)
            display(pacA,pastilha,set(listaes),caminho)
            espacos_espandidos += len(explorado)
    print("FIM: total de expandidos: " + str(espacos_espandidos))

# exercicio 2
def manhatan_goal(self,no) : 
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        return manhatan(no.state,self.goal)

    def mais_melhor_goal(self, no):
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        ponto = no.state
        
        if ponto in self.di_heuri:
            return self.di_heuri[ponto]
        else:
            return manhatan(ponto, self.goal)
            
            
            
            
            
            
            
            
            
def mais_melhor_bom_procura_graph(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    explored = set()
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node, explored
    frontier = PriorityQueue(min, f)
    frontier.append(node)
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node, explored
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
    return node

def a_estrelita(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return mais_melhor_bom_procura_graph(problem, lambda n: n.path_cost + h(n))


def modelo(pacman, obstaculos):
    modelo = []
    for xx in [-1, 0, 1]:
            for yy in [-1, 0, 1]:
                
                if (xx != 0 or yy != 0 ):
                    x = pacman[0] + xx
                    y = pacman[1] + yy
                       
                    if (x >= 0 and y >= 0 ):
                        if (x,y) in obstaculos:
                            modelo.append((x, y))

    return modelo
    
    
def recalc_heuri(pacA, casa, di_heuri, listaes, soluc):
    set_lista = set(listaes)
    problemo2grid = GridProblem(pacA, casa, set_lista, di_heuri)
    res_astar2 = a_estrelita(problemo2grid, problemo2grid.manhatan_goal)[0]
    nova = len(res_astar2.solution())
    nova_heuristica = soluc - nova
    di_heuri[casa] = nova_heuristica
    
    return


def sort_by_key(item):
    return (item[0][0], item[0][1])




def planeia_adaptativo_online(pacman, pastilha, obstaculos):
    print('MUNDO')
    display(pacman,pastilha,obstaculos)
    print('MODELO')
        
    es = modelo(pacman,obstaculos) #estado inicial
    display(pacman,pastilha,set(es))
    listaes = es

    espacos_espandidos = 0
    nr_iteracoes = 1

    di_heuri = {}
    pacA = pacman

    while pastilha != pacA:
            
                #copiar grid problem
                #g= grid....
            caminho = []
            gufi_problemo = GridProblem(pacA, pastilha, listaes, di_heuri)
            estrela_start = a_estrelita(gufi_problemo, gufi_problemo.mais_melhor_goal)[0]
            passados = a_estrelita(gufi_problemo, gufi_problemo.mais_melhor_goal)[1]
            soluc = len(estrela_start.solution())
            
            for casa in passados:
                recalc_heuri(pacA, casa, di_heuri, listaes,  soluc)

            for pac in estrela_start.path():
                listaes.extend(modelo(pacA,obstaculos))
                if not pac.state  in obstaculos:
                    #adicionar pacman
                    pacA=pac.state
                    #adicionar Path
                    caminho.append(pac.state)
                    listaes.extend(modelo(pacA,obstaculos))
                    #procurar diferenca de extend
                                
                else:
                    break


            print("ITERAÇÃO: " + str(nr_iteracoes))
            nr_iteracoes += 1
            total = len(passados)
            print(estrela_start.solution())
            print("Expandidos " + str(total))
            organizado = sorted(di_heuri.items(), key=sort_by_key)
            resultado_organizado = organizado
            print("Novas heurísticas:", resultado_organizado)
            
            espacos_espandidos += total
            #print(listaes)
            display(pacA,pastilha,set(listaes),caminho)
           
    print("FIM: total de expandidos: " + str(espacos_espandidos))