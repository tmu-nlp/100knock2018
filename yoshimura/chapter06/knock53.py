import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

for word in tree.iter('word'):
    print(word.text)
