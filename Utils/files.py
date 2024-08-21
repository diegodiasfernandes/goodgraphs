import sys
sys.path.append("..\goodgraphs")

from Utils.typehinting import *
import json
    
def readJson(json_file: str) -> dict:
    with open(json_file, 'r') as file:
        data = json.load(file)

    return data

def readMatrixTxt(txt_file: str) -> List[List[Union[float]]]:
    matrix = []
    with open(txt_file, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            matrix.append([float(value) for value in values if value.strip()])

    return matrix

def grFileToDict(gr_file: str) -> dict:
    vertices: set = set()
    edges: list = []
    with open(gr_file, 'r') as file:
        for line in file:
            if line.startswith('a'):
                parts = line.strip().split()

                vertices.add(int(parts[1]))
                edges.append([int(parts[1]), int(parts[2]), float(parts[3])])
    
    graph_dict: dict = {
        "vertices": list(vertices),
        "edges": edges
    }

    return graph_dict

if __name__ == '__main__':
    print(readMatrixTxt("examples\\adj_matrix.txt"))