from xml.etree import ElementTree as ET
from nltk.tree import ParentedTree

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()
parses = ET.fromstringlist(lines).findall('document/sentences/sentence/parse')

def s_expression(parses):
    for s_exp in parses:
        tree = ParentedTree.fromstring(s_exp.text)
        sub_trees = list(tree.subtrees())
        for sub_tree in sub_trees:
            if sub_tree.label() == 'NP':
                tokens = list(sub_tree.leaves())
                print(' '.join(tokens))

s_expression(parses)
