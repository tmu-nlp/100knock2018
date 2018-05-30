from knock41 import load_cabocha_iter
import pydot

def gen_graph(edges):
    graph = pydot.Dot(graph_type='digraph')
    graph.set_node_defaults(fontname='Sans Not-Rotated 12')

    for edge in edges:
        id1 = str(edge[0])
        label1 = edge[1]
        id2 = str(edge[2])
        label2 = edge[3]

        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        graph.add_edge(pydot.Edge(id1, id2))
    return graph


def main():
    for i, chunks in enumerate(load_cabocha_iter()):
        if i != 7:
            continue
        edges = []
        for j, chunk in enumerate(chunks):
            if chunk.dst == -1:
                continue
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if not src or not dst:
                continue
            edges.append((j, src, chunk.dst, dst))

    # グラフの書き出し
    graph = gen_graph(edges)
    print(graph.to_string())
    graph.write('graph.png', format='png', encoding='utf8')


if __name__ == '__main__':
    main()


''' 問
44. 係り受け木の可視化

与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''

''' 実行結果
digraph G {
node [fontname="Sans Not-Rotated 12"];
0 [label="この"];
1 [label="書生というのは"];
0 -> 1;
1 [label="書生というのは"];
7 [label="話である"];
1 -> 7;
2 [label="時々"];
4 [label="捕えて"];
2 -> 4;
3 [label="我々を"];
4 [label="捕えて"];
3 -> 4;
4 [label="捕えて"];
5 [label="煮て"];
4 -> 5;
5 [label="煮て"];
6 [label="食うという"];
5 -> 6;
6 [label="食うという"];
7 [label="話である"];
6 -> 7;
}
'''

