import xml.etree.ElementTree as ET



def find_SVO(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()

    for sentence in root.findall(".//sentences/sentence"):
        for dep_nsubj in sentence.findall(".//dependencies[@type='collapsed-dependencies']/dep[@type='nsubj']"):
            for dep_dobj in sentence.findall(".//dependencies[@type='collapsed-dependencies']/dep[@type='dobj']"):
                if dep_nsubj.find('governor').get('idx') == dep_dobj.find('governor').get('idx'):
                    S = dep_nsubj.find('dependent').text
                    V = dep_nsubj.find('governor').text
                    O = dep_dobj.find('dependent').text
                    yield '\t'.join([S, V, O])
                else:
                    continue


if __name__ == '__main__':
    with open('./result/knock58.txt', 'w') as data_out:
        data_in_path = '../data/knock50.txt.xml'
        for line in find_SVO(data_in_path, data_out):
            print(line, file=data_out)
