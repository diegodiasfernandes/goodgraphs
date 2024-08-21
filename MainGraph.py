from Utils.typehinting import *
from Utils.files import readJson, readMatrixTxt
import math

class MainGraph:
    def __init__(self, data: dict | list[list[Union[int, float]]]) -> None:
        self.n: int = 0
        self.m: int = 0
        self.mind: int | None = 0
        self.maxd: int | None = 0
        self.vertices: list[int] = [-1]
        self.adjList = self.getAdjacencyList(data)
        self.adjustAttributes()

        from SearchClasses import DFS, BFS, Dijkstra
        self.dfs: DFS.DFS | None = None
        self.bfs: BFS.BFS | None = None
        self.dijks: Dijkstra.Dijkstra | None = None
        
    def adjustAttributes(self) -> None:
        self.n = len(self.adjList)
        self.m = 0
        self.mind = None
        self.maxd = None
        self.vertices = [v for v in self.adjList]
        for vertex in self.adjList:
            deg = len(self.adjList[vertex])
            self.m += deg

            if self.mind is None or self.mind > deg:
                self.mind = deg
            if self.maxd is None or self.maxd < deg:
                self.maxd = deg
    
    def neighbors(self, vertex: int):
        neighbs: list[int] = []
        for e in self.adjList[vertex]:
            neighbs.append(e[0])

        return neighbs

    def weight(self, u: int, v: int) -> float | None:
        for neighbor in range(len(self.adjList[u])):
            if v == self.adjList[u][neighbor][0]:
                return self.adjList[u][neighbor][1]
        
        return None

    def DFS(self, initial: int = 0):
        if self.dfs is None:
            if initial not in self.vertices: initial = self.vertices[0]
            from SearchClasses.DFS import DFS
            self.dfs = DFS(self)
            self.dfs.start(initial)
        
        return self.dfs.pi, self.dfs.t_init, self.dfs.t_finish

    def DFSShowResults(self):
        if self.dfs is None:
            print("dfs not initializes yet. Run self.DFS()")
            return None
        
        self.dfs.showResults()

    def BFS(self, initial: int = 0):
        if self.bfs is None:
            if initial not in self.vertices: initial = self.vertices[0]
            from SearchClasses.BFS import BFS
            self.bfs = BFS(self)
            self.bfs.start(initial)
        
        return self.bfs.pi, self.bfs.distance

    def BFSShowResults(self):
        if self.bfs is None:
            print("bfs not initializes yet. Run self.BFS()")
            return None
        
        self.bfs.showResults()

    def dijkstra(self, initial: int = 0):
        if self.dijks is None:
            if initial not in self.vertices: initial = self.vertices[0]
            from SearchClasses.Dijkstra import Dijkstra
            self.dijks = Dijkstra(self)
            self.dijks.start(initial)
        
        return self.dijks.pi, self.dijks.distance
    
    def minPathDijkstra(self, u: int, v : int):
        if self.dijks is None:
            self.dijkstra(u)

        return self.dijks.minPath(u, v)

    def printGraph(self) -> None:
        print("="*40)
        print("Adjacency List: ")
        for i in self.adjList:
            print(" " + str(i) + ": " + str(self.adjList[i]))

    def getAdjacencyList(self, data: dict | list[list[Union[int, float]]]) -> Dict[int, List[tuple[int, float]]]:
        raise NotImplementedError("Subclasses should implement this method.")

    def degree(self, vertex: int):
        raise NotImplementedError("Subclasses should implement this method.")