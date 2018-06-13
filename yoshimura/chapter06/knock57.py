import xml.etree.ElementTree as ET
import pydot_ng as pydot

tree = ET.parse('nlp.txt.xml')

path_sentence = './document/sentences/sentence'
path_dep = './dependencies[@type="collapsed-dependencies"]/dep'

for sentence in tree.iterfind(path_sentence):
    sentence_id = int(sentence.get('id'))

    edges = []
    for dep in sentence.iterfind(path_dep):
        gov = dep.find('./governor')
        dep = dep.find('./dependent')

        gov_id, gov_txt = gov.get('idx'), gov.text
        dep_id, dep_txt = dep.get('idx'), dep.text

        # edges.append(((gov_id, gov_txt), (dep_id, dep_txt)))
        edges.append((gov_txt, dep_txt))
    
    # グラフを描画
    graph = pydot.graph_from_edges(edges, directed=True)
    graph.write_png(f'{sentence_id}.png')
