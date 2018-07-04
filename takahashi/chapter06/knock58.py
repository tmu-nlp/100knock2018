# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from graphviz import Digraph

file_name = 'out_knock50.txt.xml'

root = ET.parse(file_name)
ret = {}

for sentence in root.iterfind('./document/sentences/sentence'):
    sentence_id = int(sentence.get('id'))

    nodes = {}
    nsubjs = {}
    dobjs = {}
    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        dept_type = dep.get('type')
        if dept_type == 'nsubj' or dept_type == 'dobj':
            govr = dep.find('./governor')
            dept = dep.find('./dependent')
            if dept_type == 'nsubj':
                nsubjs[govr.get('idx')] = dept.get('idx')
            if dept_type == 'dobj':
                dobjs[govr.get('idx')] = dept.get('idx')
            nodes[govr.get('idx')] = govr.text
            nodes[dept.get('idx')] = dept.text

    for dobj in dobjs.keys():
        if dobj in nsubjs.keys():
            print(''.join('{0}\t{1}\t{2}'.format(nodes[nsubjs[dobj]], nodes[dobj], nodes[dobjs[dobj]])))
