# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from graphviz import Digraph

file_name = 'out_knock50.txt.xml'

root = ET.parse(file_name)
ret = {}


for sentence in root.iterfind('./document/sentences/sentence'):
    sentence_id = int(sentence.get('id'))

    nodes = {}
    edges = []
    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        if dep.get('type') != 'punct':
            govr = dep.find('./governor')
            dept = dep.find('./dependent')
            edges.append((govr.get('idx'), dept.get('idx')))
            nodes[govr.get('idx')] = govr.text
            nodes[dept.get('idx')] = dept.text

    graph = Digraph(format='png')
    graph.attr('node', shape='circle')

    for key, value in nodes.items():
        graph.node(key, label=value)

    for edge in edges:
        graph.edge(edge[0], edge[1])
    graph.render('binary_tree_graphviz_{}'.format(sentence_id))
