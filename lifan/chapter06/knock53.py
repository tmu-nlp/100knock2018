import xml.etree.ElementTree as ET

tree = ET.parse('../files/nlp.txt.xml')
root = tree.getroot()

for child in root[0][1].iter('word'):
    print(child.text)
