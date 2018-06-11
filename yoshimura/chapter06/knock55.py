import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

for token in tree.iter('token'):
    if token.findtext('NER') == 'PERSON':
        print(token.findtext('word'))
