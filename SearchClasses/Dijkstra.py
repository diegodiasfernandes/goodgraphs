import sys
sys.path.append("..\goodgraphs")

import heapq
import math
from Utils.typehinting import *
from Graph import Graph
from Digraph import Digraph

class Dijkstra:
    def __init__(self, graph: Graph | Digraph) -> None:
        self.pi: Dict[int, Union[int, None]] = {v: None for v in graph.vertices}
        self.distance: Dict[int, float] = {v: math.inf for v in graph.vertices}

        self.graph = graph

        self.last_initial: int | None = None
    
    def start(self, initial: int = 0) -> None:
        self.distance[initial] = 0
        heap = [(0, initial)]

        while heap:
            u_d, u = heapq.heappop(heap)

            if not(u_d > self.distance[u]):
                for neighbor in self.graph.neighbors(u):
                    weight = self.graph.weight(u, neighbor)
                    distance = u_d + weight

                    if distance < self.distance[neighbor]:
                        self.distance[neighbor] = distance
                        self.pi[neighbor] = u
                        heapq.heappush(heap, (distance, neighbor))
        
        self.last_initial = initial
    
    def minPath(self, u: int, v: int):
        if self.last_initial is None or self.last_initial != u:
            self.start(u)
        
        path = []
        curr_vertex = v
        while curr_vertex is not None:
            path.append(curr_vertex)
            curr_vertex = self.pi[curr_vertex]
        
        path.reverse()

        return path, self.distance[v]