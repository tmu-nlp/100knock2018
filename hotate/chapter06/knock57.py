# -*- coding: utf-8 -*-
from graphviz import Digraph
import xml.etree.ElementTree as ET


if __name__ == '__main__':
    tree = ET.parse('knock50.txt.xml')

    sentences = []
    i = 0
    for dep in tree.iter('dependencies'):
        sentence = []
        if dep.attrib['type'] == 'collapsed-dependencies':
            for d in dep.iter('dep'):
                no = f'[{len(sentences)}] '
                governor = no + d.find('governor').text
                dependent = no + d.find('dependent').text
                sentence.append([governor, dependent])
            sentences.append(sentence)

    G = Digraph(format='png')
    G.attr('node', shape='circle')

    for i, sentence in enumerate(sentences):
        if i < 5:
            for pair in sentence:
                G.edge(pair[0], pair[1])
    G.render('binary_tree_graphviz')
