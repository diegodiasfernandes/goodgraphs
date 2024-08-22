import math
from Utils.typehinting import *
from Graph import Graph
from Digraph import Digraph

class BFS:
    def __init__(self, graph: Graph | Digraph) -> None:
        self.color: Dict[int, Literal["white", "gray", "black"]] = {v: "white" for v in graph.vertices}
        self.pi: Dict[int, Union[int, None]] = {v: None for v in graph.vertices}
        self.distance: Dict[int, float] = {v: math.inf for v in graph.vertices}
        self.graph = graph

        self.last_initial: int | None = None

    def start(self, initial: int = 0) -> None:
        if self.last_initial == initial: 
            return None
        
        self.distance[initial] = 0
        self.color[initial] = 'gray'

        stack = [initial]
        while stack:
            u = stack.pop()
            for neighbor in self.graph.neighbors(u):
                if self.color[neighbor] == 'white':
                    self.color[neighbor] = 'gray'
                    self.distance[neighbor] = self.distance[u] + 1
                    self.pi[neighbor] = u
                    stack.append(neighbor)

            self.color[u] = 'black'
        
        self.last_initial = initial
    
    def showResults(self):
        print("--------------------------------------------")
        print(" Vertex | Distance | Predecessor (pi)")
        print("--------------------------------------------")
        for v in self.graph.vertices:
            space0: str = " " * (6 - math.floor(math.log10(max(1, v))))
            if self.distance[v] != math.inf:
                space1: str = " " * (9 - math.floor(math.log10(max(1, self.distance[v]))))
            else:
                space1: str = " " * (9 - 2)
            print(f" {v}{space0}|{self.distance[v]}{space1}|{self.pi[v]}")