import xml.etree.ElementTree as ET
from itertools import islice


def is_person(token):
    '''引数のtokenが人名かどうかをboolで返す'''
    return token.findtext('NER') == 'PERSON'


def main(n=None):
    root = ET.parse('knock50.txt.xml')

    for name in islice((token.findtext('word') for token in root.iter('token') if is_person(token)), n):
        print(name)


if __name__ == '__main__':
    main()


''' 問
55. 固有表現抽出

入力文中の人名をすべて抜き出せ．
'''

''' 実行結果
Alan
Turing
Joseph
Weizenbaum
MARGIE
Schank
Wilensky
Meehan
Lehnert
Carbonell
Lehnert
Racter
Jabberwacky
Moore
'''
