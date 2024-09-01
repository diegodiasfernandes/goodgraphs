from Utils.typehinting import *
from MainGraph import MainGraph

class Digraph(MainGraph):
    def getAdjacencyList(self, data: dict | list[list[Union[int, float]]]) -> Dict[int, List[tuple[int, float]]]:
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

        if not(graph['graph_type'] != 'undirected' or graph['graph_type'] is not None): 
            raise ValueError("Not a Graph! Try Digraph.getAdjacencyList()")

        adj_list: Dict[ int, List[tuple[int, float]] ] = {}
        for vertex in graph["vertices"]:
            adj_list[vertex] = []

        for edge in graph['edges']:
            vertex_A: int = edge[0]
            vertex_B: int = edge[1]
            weight: float = edge[2]

            adj_list[vertex_A].append((vertex_B, weight))
        
        return adj_list
    
    def adjustAttributes(self) -> None:
        self.n = len(self.adjList)
        self.m = 0
        self.vertices = [v for v in self.adjList]
        degrees = {v:0 for v in self.vertices}
        for vertex in self.adjList:
            num_edges = len(self.adjList[vertex])
            self.m += num_edges

            for edge in self.adjList[vertex]:
                degrees[vertex] += 1
                degrees[edge[0]] -= 1

        self.mind = min(degrees.values())
        self.maxd = max(degrees.values())

    def degree(self, vertex: int) -> int:
        deg: int = len(self.adjList[vertex])
        for v in self.adjList:
            for e in self.adjList[v]:
                if e[0] == vertex:
                    deg -= 1

        return deg