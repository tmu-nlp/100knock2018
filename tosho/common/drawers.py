import os,sys
sys.path.append(os.pardir)

from common.morph import Morph, Chunk
import pydot

def draw_dependency_graph(chunks, filename='graph.png'):
    graph = pydot.Dot(graph_type='graph')

    for chunk in chunks:
        if chunk.dst is not None:
            src = chunk.sentence(True)
            dst = chunks[chunk.dst].sentence(True)

            edge = pydot.Edge(dst, src)
            graph.add_edge(edge)
    
    graph.write_png(filename)
