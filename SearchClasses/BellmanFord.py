import sys
sys.path.append("goodgraphs")

import math
from Utils.typehinting import *
from Graph import Graph
from Digraph import Digraph

class BellmanFord:
    def __init__(self, graph: Graph | Digraph) -> None:
        self.pi: Dict[int, Union[int, None]] = {v: None for v in graph.vertices}
        self.distance: Dict[int, float] = {v: math.inf for v in graph.vertices}

        self.graph = graph

        self.last_initial: int | None = None

    def start(self, initial: int = 0) -> None:
        self.distance[initial] = 0
        
        V = len(self.graph.vertices)

        for _ in range(V - 1):
            for u in self.graph.vertices:
                for v, weight in self.graph.adjList[u]:
                    if self.distance[u] != math.inf and self.distance[u] + weight < self.distance[v]:
                        self.distance[v] = self.distance[u] + weight
                        self.pi[v] = u

        for u in self.graph.vertices:
            for v, weight in self.graph.adjList[u]:
                if self.distance[u] != math.inf and self.distance[u] + weight < self.distance[v]:
                    raise ValueError("Grafo com ciclos negativos!")
