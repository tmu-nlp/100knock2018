# -*- coding: utf-8 -*-

from knock41 import chunk_list
from knock42 import srcs_dst_list
from graphviz import Digraph
import pydot


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    list_srcs_dst = srcs_dst_list(sentences)
    edge = []
    for i, line in enumerate(list_srcs_dst):
        if i < 10:
            for pair in line:
                edge.append((str(pair[0].phrase_surface()), str(pair[1].phrase_surface())))
                G.edge(str(pair[0].phrase_surface()), str(pair[1].phrase_surface()))
    G.render('binary_tree_graphviz')
    g = pydot.graph_from_edges(edge)
    g.write_jpeg('binary_tree_pydot.png', prog='dot')

    # for i, (dst, srcs) in enumerate(list_srcs_dst.items()):
    #     if i < 100:
    #         edge.append((str(dst.phrase_surface()), str(srcs.phrase_surface())))
    #         G.edge(str(dst.phrase_surface()), str(srcs.phrase_surface()))
    # G.render('binary_tree_graphviz')
    # g = pydot.graph_from_edges(edge)
    # g.write_jpeg('binary_tree_pydot.png', prog='dot')
