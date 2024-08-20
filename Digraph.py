from Utils.typehinting import *
from Utils.files import readJson, readMatrixTxt

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
        self.mind: int = 0
        self.maxd: int = 0
        self.vertices: list[int] = [-1]
        self.adjList = self.getAdjacencyList(data)
        self.adjustAttributes()
        
    def adjustAttributes(self) -> None:
        self.n = len(self.adjList)
        self.m = 0
        self.mind = None
        self.maxd = None
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
        return self.adjList[vertex]

    def printGraph(self) -> None:
        print("="*40)
        print("Adjacency List: ")
        for i in range(len(self.adjList)):
            print(" " + str(i) + ": " + str(self.adjList[i]))

if __name__ == '__main__':
    data = readJson("examples\\dir_weights_1.json")
    graph = Digraph(data)
    graph.printGraph()
    print(graph.n)
    print(graph.m)
    print(graph.mind)
    print(graph.maxd)
    print(graph.neighbors(3))