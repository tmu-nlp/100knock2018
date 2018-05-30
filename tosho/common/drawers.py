import os,sys
sys.path.append(os.pardir)

from common.morph import Morph, Chunk
import pydot

def draw_dependency_graph(chunks, filename='graph.png'):
    graph = pydot.Dot(graph_type='graph')

    for chunk in chunks:
        if chunk.dst > -1:
            src = chunk.phrase(True)
            dst = chunks[chunk.dst].phrase(True)

            edge = pydot.Edge(dst, src)
            graph.add_edge(edge)
    
    graph.write_png(filename)
