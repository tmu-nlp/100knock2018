import xml.etree.ElementTree as ET
import pydot_ng as pydot

tree = ET.parse('nlp.txt.xml')

path_sentence = './document/sentences/sentence'
path_dep = './dependencies[@type="collapsed-dependencies"]/dep'

for sentence in tree.iterfind(path_sentence):
    sentence_id = int(sentence.get('id'))

    edges = []
    for dep in sentence.iterfind(path_dep):
        if dep.get('type') != 'punct':
            gove = dep.find('./governor')
            depe = dep.find('./dependent')
            edges.append((gove.text + '_' + gove.get('idx'), depe.text + '_' + depe.get('idx')))

    # for t in edges:
    #     print(t)

    # グラフを描画
    graph = pydot.graph_from_edges(edges, directed=True)
    graph.write_png(f'{sentence_id}.png')

