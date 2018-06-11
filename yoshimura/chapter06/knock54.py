import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

for token in tree.iter('token'):
    word = token.findtext('word')
    lemma = token.findtext('lemma')
    pos = token.findtext('POS')
    print(f'{word}\t{lemma}\t{pos}')