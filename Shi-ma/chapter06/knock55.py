import xml.etree.ElementTree as ET

def find_person(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for sentence in root.findall(".//sentences/sentence"):
        for token in sentence.findall(".//token"):
            if token.find('NER').text == 'PERSON':
                yield token.find('word').text
            else:
                continue


if __name__ == '__main__':
    with open('./result/knock55.txt', 'w') as data_out:
        data_in_path = '../data/knock50.txt.xml'
        for line in find_person(data_in_path, data_out):
            print(line, file=data_out)
