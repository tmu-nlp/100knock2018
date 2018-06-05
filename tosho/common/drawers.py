import os,sys
sys.path.append(os.pardir)

from common.morph import Morph, Chunk
import pydot

def draw_corenlp_dependencies(deps, file_name='graph.png'):
    graph = pydot.Dot(graph_type='graph')

    for d in deps:
        edge = pydot.Edge(d.governor, d.dependent)
        graph.add_edge(edge)
    
    graph.write_png(file_name)

def draw_dependency_graph(chunks, filename='graph.png'):
    graph = pydot.Dot(graph_type='graph')

    for chunk in chunks:
        if chunk.dst > -1:
            src = chunk.phrase(True)
            dst_id = chunks[chunk.dst].id
            dst = chunks[chunk.dst].phrase(True)

            edge = pydot.Edge(f'{dst_id}:{dst}', f"{chunk.id}:{src}")
            graph.add_edge(edge)
            
    graph.write_png(filename)
