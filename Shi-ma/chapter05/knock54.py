import xml.etree.ElementTree as ET

def make_corenlp_word(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for sentence in root.findall(".//sentences/sentence"):
        for word, lemma, pos in zip(sentence.findall(".//token/word"), sentence.findall(".//token/lemma"), sentence.findall(".//token/POS")):
            yield '\t'.join([word.text, lemma.text, pos.text])
        yield ''


if __name__ == '__main__':
    with open('./result/knock54.txt', 'w') as data_out:
        data_in_path = '../data/knock50.txt.xml'
        for line in make_corenlp_word(data_in_path, data_out):
            print(line, file=data_out)
