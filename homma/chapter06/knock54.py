import xml.etree.ElementTree as ET
from itertools import islice


def main(n=None):
    root = ET.parse('knock50.txt.xml')
    for token in islice(root.iter('token'), n):
        word  = token.findtext('word')
        lemma = token.findtext('lemma')
        pos   = token.findtext('POS')
        print(f'{word}\t{lemma}\t{pos}')


if __name__ == '__main__':
    main(10)


''' 問
54. 品詞タグ付け

Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
'''

''' 実行結果
Natural natural JJ
language        language        NN
processing      processing      NN
From    from    IN
Wikipedia       Wikipedia       NNP
,       ,       ,
the     the     DT
free    free    JJ
encyclopedia    encyclopedia    NN
Natural natural JJ
'''
