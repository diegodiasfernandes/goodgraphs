import sys
sys.path.append("..\goodgraphs")

from Utils.typehinting import *
import math
from Graph import Graph
from Digraph import Digraph

class DFS:
    def __init__(self, graph: Graph | Digraph) -> None:
        self.color: Dict[int, Literal["white", "gray", "black"]] = {v: "white" for v in graph.vertices}
        self.pi: Dict[int, Union[int, None]] = {v: None for v in graph.vertices}
        self.t_init: Dict[int, int] = {v: 0 for v in graph.vertices}
        self.t_finish: Dict[int, int] = {v: 0 for v in graph.vertices}
        self.time: int = 0
        self.graph = graph

    def start(self, initial: int = 0):
        vertices = self.graph.vertices
        vertices = [v for v in self.graph.vertices if v != initial]
        self.search(initial)

        for v in vertices:
            if self.color[v] == 'white':
                self.search(v)
    
    def search(self, vertex: int):
        self.time += 1
        self.t_init[vertex] = self.time
        self.color[vertex] = "gray"

        for neighbor in self.graph.neighbors(vertex):
            if self.color[neighbor] == "white":
                self.pi[neighbor] = vertex
                self.search(neighbor)
        
        self.color[vertex] = "black"
        self.time += 1
        self.t_finish[vertex] = self.time

    def showResults(self):
        print("--------------------------------------------")
        print(" Vertex | Start | Finish | Predecessor (pi)")
        print("--------------------------------------------")
        for v in self.graph.vertices:
            space0: str = " " * (6 - math.floor(math.log10(max(1, v))))
            space1: str = " " * (6 - math.floor(math.log10(max(1, self.t_init[v]))))
            space2: str = " " * (7 - math.floor(math.log10(max(1, self.t_finish[v]))))
            print(f" {v}{space0}|{self.t_init[v]}{space1}|{self.t_finish[v]}{space2}|{self.pi[v]}")