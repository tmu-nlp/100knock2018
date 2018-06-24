# CoreNLPをダウンロードし展開した後そのディレクトリに移動して、
# ./corenlp.sh -ssplit.eolonly -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file ../../chapter06/result/knock50.txt -outputDirectory ../../data/
# を実行

import xml.etree.ElementTree as ET

def make_corenlp_word(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for sentence in root.findall(".//sentences/sentence"):
        for word in sentence.findall(".//word"):
            yield word.text
        yield ''


if __name__ == '__main__':
    with open('./result/knock53.txt', 'w') as data_out:
        data_in_path = '../data/knock50.txt.xml'
        for word in make_corenlp_word(data_in_path, data_out):
            print(word, file=data_out)
