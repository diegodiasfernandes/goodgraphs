from Utils.typehinting import *
from Utils.files import readGraphJson

class Graph:
    def __init__(self, graph: GraphDict) -> None:
        '''
        example of graph:
        adjacencyList = {
            0: [(1, 1)]
            1: [(0, 1), (2, 1)]
            2: [(1, 1)]
        }
        '''

        self.adjacencyList: Dict[int, List[tuple[int, float]]] | None = self.getAdjacencyList(graph)

    def getAdjacencyList(self, graph: GraphDict) -> Dict[ int, List[tuple[int, float]] ]:
        if graph['graph_type'] != 'undirected': raise ValueError("Not a Graph! Try Digraph.getAdjacencyList()")

        adj_list: Dict[ int, List[tuple[int, float]] ] = {}
        for vertex in graph["vertices"]:
            adj_list[vertex] = []

        for edge in graph['edges']:
            vertex_A: int = edge[0]
            vertex_B: int = edge[1]
            weight: float = edge[2]

            adj_list[vertex_A].append((vertex_B, weight))
            adj_list[vertex_B].append((vertex_A, weight))
        
        return adj_list
    
    def printGraph(self) -> None:
        print("="*40)
        print("Adjacency List: ")
        for i in range(len(self.adjacencyList)):
            print(" " + str(i) + ": " + str(self.adjacencyList[i]))

if __name__ == '__main__':
    json_graph = readGraphJson("examples\graph2.json")
    graph = Graph(json_graph)
    graph.printGraph()