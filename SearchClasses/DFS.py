import sys
sys.path.append("..\goodgraphs")

from Utils.typehinting import *
from Utils.files import readJson, readMatrixTxt
import math
from Graph import Graph
from Digraph import Digraph

class DFS:
    def __init__(self, graph: Graph | Digraph) -> None:
        self.color: Dict[int, Literal["white", "gray", "black"]] = {v: "white" for v in graph.vertices}
        self.parent: Dict[int, Union[int, None]] = {v: None for v in graph.vertices}
        self.start_time: Dict[int, int] = {v: 0 for v in graph.vertices}
        self.finish_time: Dict[int, int] = {v: 0 for v in graph.vertices}
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
        self.start_time[vertex] = self.time
        self.color[vertex] = "gray"

        for neighbor in self.graph.neighbors(vertex):
            if self.color[neighbor] == "white":
                self.parent[neighbor] = vertex
                self.search(neighbor)
        
        self.color[vertex] = "black"
        self.time += 1
        self.finish_time[vertex] = self.time

    def showResults(self):
        print(" Vertex | Start | Finish | Parent")
        print("------------------------------------")
        for v in self.graph.vertices:
            space0: str = " " * (6 - math.floor(math.log10(max(1, v)))) # type ignore
            space1: str = " " * (6 - math.floor(math.log10(max(1, self.start_time[v])))) # type ignore
            space2: str = " " * (7 - math.floor(math.log10(max(1, self.finish_time[v])))) # type ignore
            print(f" {v}{space0}|{self.start_time[v]}{space1}|{self.finish_time[v]}{space2}|{self.parent[v]}")