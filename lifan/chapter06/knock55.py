import xml.etree.ElementTree as ET

tree = ET.parse('../files/nlp.txt.xml')

for token in tree.iter('token'):
    word = token.findtext('word')
    if token.findtext('NER') == "PERSON":
    	print(f'{word}')
