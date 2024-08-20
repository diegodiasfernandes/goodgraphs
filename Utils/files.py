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

if __name__ == '__main__':
    print(readMatrixTxt("examples\\adj_matrix.txt"))