import sys
sys.path.append("..\goodgraphs")

from Utils.typehinting import *
import json

def readGraphsJson(json_file: str) -> list[GraphDict]:
    with open(json_file, 'r') as file:
        data = json.load(file)

    all_graphs = []
    
    for graph in data['graphs']:
        for edge in graph['edges']:
            if len(edge) == 2:
                edge.append(1)

        g: GraphDict = {
            'graph_type': graph['type'],
            'vertices': graph['vertices'],
            'edges': graph['edges']
        }

        all_graphs.append(g)
        
        '''print(f"Graph Type: {graph['type']}")
        print(f"Vertices: {graph['vertices']}")
        print(f"Edges: {graph['edges']}")
        print("-" * 40)'''

    return all_graphs
    
def readGraphJson(json_file: str) -> GraphDict:
    with open(json_file, 'r') as file:
        data = json.load(file)

    for edge in data['edges']:
        if len(edge) == 2:
            edge.append(1)

    graph: GraphDict = {
        'graph_type': data['type'],
        'vertices': data['vertices'],
        'edges': data['edges']
    }

    '''print(f"Graph Type: {data['type']}")
    print(f"Vertices: {data['vertices']}")
    print(f"Edges: {data['edges']}")
    print("-" * 40)'''

    return graph

if __name__ == '__main__':
    readGraphJson("examples\graph1.json")