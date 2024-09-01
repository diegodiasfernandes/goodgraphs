from Utils.typehinting import *
import math
from MainGraph import MainGraph

class DFS:
    def __init__(self, graph: MainGraph) -> None:
        self.color: Dict[int, Literal["white", "gray", "black"]] = {v: "white" for v in graph.vertices}
        self.pi: Dict[int, Union[int, None]] = {v: None for v in graph.vertices}
        self.t_init: Dict[int, int] = {v: 0 for v in graph.vertices}
        self.t_finish: Dict[int, int] = {v: 0 for v in graph.vertices}
        self.time: int = 0
        self.graph = graph

        self.last_initial: int | None = None

    def start(self, initial: int = 0) -> None:
        if self.last_initial == initial: 
            return None
        
        vertices = [v for v in self.graph.vertices if v != initial]

        self.search(initial)

        for v in vertices:
            if self.color[v] == 'white':
                self.search(v)
        
        self.last_initial = initial

    def search(self, vertex: int):
        stack = [(vertex, iter(self.graph.neighbors(vertex)))]

        while stack:
            current_vertex, neighbors = stack[-1]
            if self.color[current_vertex] == 'white':
                self.time += 1
                self.t_init[current_vertex] = self.time
                self.color[current_vertex] = 'gray'

            try:
                neighbor = next(neighbors)
                if self.color[neighbor] == 'white':
                    self.pi[neighbor] = current_vertex
                    stack.append((neighbor, iter(self.graph.neighbors(neighbor))))
            except StopIteration:
                self.color[current_vertex] = 'black'
                self.time += 1
                self.t_finish[current_vertex] = self.time
                stack.pop()

    def showResults(self):
        print("--------------------------------------------")
        print(" Vertex | Start | Finish | Predecessor (pi)")
        print("--------------------------------------------")
        for v in self.graph.vertices:
            space0 = " " * (6 - math.floor(math.log10(max(1, v))))
            space1 = " " * (6 - math.floor(math.log10(max(1, self.t_init[v]))))
            space2 = " " * (7 - math.floor(math.log10(max(1, self.t_finish[v]))))
            print(f" {v}{space0}|{self.t_init[v]}{space1}|{self.t_finish[v]}{space2}|{self.pi[v]}")