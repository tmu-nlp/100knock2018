# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from collections import defaultdict


if __name__ == '__main__':
    tree = ET.parse('knock50.txt.xml')

    l = []
    for dependencies in tree.iter('dependencies'):
        if dependencies.attrib['type'] == 'collapsed-dependencies':
            nsubj = defaultdict(str)
            dobj = defaultdict(str)
            for dep in dependencies.iter('dep'):
                governor = dep.find('governor').text
                dependent = dep.find('dependent').text
                if dep.attrib['type'] == 'nsubj':
                    nsubj[governor] = dependent
                elif dep.attrib['type'] == 'dobj':
                    dobj[governor] = dependent
            for pre, sub in nsubj.items():
                if dobj[pre] != '':
                    l.append(f'{sub}\t{pre}\t{dobj[pre]}')
                    dobj[pre] = ''
                else:
                    l.append(f'{sub}\t{pre}')
            for pre, obj in dobj.items():
                if obj != '':
                    l.append(f'{pre}\t{obj}')

    for s in l:
        print(s)

