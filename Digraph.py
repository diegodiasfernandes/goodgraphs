from Utils.typehinting import *
from Utils.files import readJson, readMatrixTxt
import math

class Digraph:
    def __init__(self, data: dict | list[list[Union[int, float]]]) -> None:
        '''
        example of graph:
        adjacencyList = {
            0: [(1, 2.75)]
            1: [(2, 3.91)]
            2: []
        }
        '''
        self.n: int = 0
        self.m: int = 0
        self.mind: int | None = 0
        self.maxd: int | None = 0
        self.vertices: list[int] = [-1]
        self.adjList = self.getAdjacencyList(data)
        self.adjustAttributes()

        from SearchClasses.DFS import DFS
        self.dfs: DFS | None = None
        
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

    def getAdjacencyList(self, data: dict | list[list[Union[int, float]]]) -> Dict[ int, List[tuple[int, float]] ]:
        def readGraphJson(data: dict) -> GraphDict:
            try:
                t = data['type']
            except:
                data['type'] = 'undirected'

            for edge in data['edges']:
                if len(edge) == 2:
                    edge.append(1)

            graph: GraphDict = {
                'graph_type': data['type'],
                'vertices': data['vertices'],
                'edges': data['edges']
            }

            return graph
        
        def readAdjMatrixTxt(data: list[list[float]]) -> GraphDict:
            vertices = list(range(len(data)))

            edges = []
            for i in vertices:
                for j in vertices:
                    if data[i][j] != 0:
                        edges.append((i, j, data[i][j]))
            
            graph: GraphDict = {
                'graph_type': 'directed',
                'vertices': vertices,
                'edges': edges
            }

            return graph

        graph: GraphDict = { 'graph_type': None, 'vertices': [0], 'edges': [(0, 0, 0)] }
        if type(data) == dict:
            graph = readGraphJson(data)
        elif type(data) == list:
            graph = readAdjMatrixTxt(data)

        if not(graph['graph_type'] != 'undirected' or graph['graph_type'] is not None): raise ValueError("Not a Graph! Try Digraph.getAdjacencyList()")

        adj_list: Dict[ int, List[tuple[int, float]] ] = {}
        for vertex in graph["vertices"]:
            adj_list[vertex] = []

        for edge in graph['edges']:
            vertex_A: int = edge[0]
            vertex_B: int = edge[1]
            weight: float = edge[2]

            adj_list[vertex_A].append((vertex_B, weight))
        
        return adj_list
    
    def neighbors(self, vertex: int):
        neighbs: list[int] = []
        for e in self.adjList[vertex]:
            neighbs.append(e[0])

        return neighbs
    
    def degree(self, vertex: int):
        deg: int = len(self.adjList[vertex])
        for v in self.adjList:
            for e in self.adjList[v]:
                if e[0] == vertex:
                    deg -= 1

        return deg
    
    def weight(self, u: int, v: int) -> float:
        for neighbor in range(len(self.adjList[u])):
            if v == self.adjList[u][neighbor][0]:
                return self.adjList[u][neighbor][1]
        
        return 0.0

    def dfsStart(self, initial: int = 0):
        if initial not in self.vertices: initial = self.vertices[0]
        from SearchClasses.DFS import DFS
        self.dfs = DFS(self)
        self.dfs.start(initial)

    def dfsAttributes(self):
        if self.dfs is None:
            print("dfs not initializes yet. Run self.dfsStart()")
            return None
        
        return self.dfs.pi, self.dfs.t_init, self.dfs.t_finish

    def dfsShowResults(self):
        if self.dfs is None:
            print("dfs not initializes yet. Run self.dfsStart()")
            return None
        
        self.dfs.showResults()

    def printGraph(self) -> None:
        print("="*40)
        print("Adjacency List: ")
        for i in self.adjList:
            print(" " + str(i) + ": " + str(self.adjList[i]))

if __name__ == '__main__':
    data = readMatrixTxt("examples\\adj-matrixes\\adj_matrix2.txt")
    #data = readJson("examples\\graph1.json")
    graph = Digraph(data)
    graph.printGraph()
    graph.dfsStart(6)
    graph.dfsShowResults()
    print(graph.vertices)