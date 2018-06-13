from xml.etree import ElementTree as ET

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()

root = ET.fromstringlist(lines)

for ele in root.findall("document/sentences/sentence/tokens/token"):
    ele_txt = []
    for child in ele.getchildren():
        if child.tag in ('word', 'lemma', 'POS'):
            ele_txt.append(child.text)
    print('\t'.join(ele_txt))

