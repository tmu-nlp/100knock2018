from pydot import Dot, Node, Edge
from xml.etree import ElementTree as ET

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()
sentences = ET.fromstringlist(lines).findall('document/sentences/sentence')

def plot_tree(sent_id):
    global sentences

    graph = Dot(graph_type='digraph')

    basic_dependencies = sentences[sent_id].findall("./dependencies[@type='collapsed-dependencies']/dep")
    for dep in basic_dependencies:

        gov = "{}\n{}".format(dep[0].get("idx"), dep[0].text)
        dep = "{}\n{}".format(dep[1].get("idx"), dep[1].text)
        graph.add_node(Node(gov))
        graph.add_node(Node(dep))
        graph.add_edge(Edge(dep, gov))
    graph.write_png(f"sentence_{sent_id}.png")

plot_tree(3)
