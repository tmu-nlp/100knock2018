from xml.etree import ElementTree as ET

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()

root = ET.fromstringlist(lines)

for tokens in root.findall("document/sentences/sentence/tokens"):
    person_tokens = (tok for tok in tokens.findall('token') if tok.find('NER').text == 'PERSON')
    full_names = []
    last_id = None
    for name in person_tokens:
        _id = int(name.attrib['id'])
        if last_id is None or last_id + 1 != _id:
            last_id = _id
            full_names.append(name.find('word').text)
        elif last_id + 1 == _id:
            last_id = _id
            full_names[-1] += ' ' + name.find('word').text
    if full_names:
        print(', '.join(full_names) + '.')

