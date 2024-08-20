import sys
sys.path.append("..\goodgraphs")

from typing import TypedDict, List, Union, Dict, Literal

class GraphDict(TypedDict):
    graph_type: Literal['undirected', 'directed', None]
    vertices: List[int]
    edges: List[tuple[int, int, float]]