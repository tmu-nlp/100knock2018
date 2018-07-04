import pydot
from knock42 import *

def draw(sent):
    graph = pydot.Dot(graph_type='digraph')
    for c, d in get_dep(sent):
        edge = pydot.Edge(to_str(c), to_str(d))
        graph.add_edge(edge)

    graph.write_png('%d.png' % idx)

if __name__ == '__main__':
    idx = int(argv[1])
    sent = get_sentence(neko_sent(idx))
    if sent is None:
        ValueError('%d. sentence is None' % idx)
    draw(sent)
