import re
from collections import defaultdict
from pprint import pprint


def load_morphems(file='neko.txt.mecab'):
    # MeCabの出力フォーマット
    # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    morphemes = []
    for line in open(file, encoding='utf8'):
        # EOS のみの行をスキップ
        if line == 'EOS\n':
            continue
        # 要素ごとに分割
        splited = re.split('[\t,]', line.strip())
        # 各形態素を格納
        morpheme = {
            'surface': splited[0],
            'base'   : splited[7],
            'pos'    : splited[1],
            'pos1'   : splited[2],
        }
        morphemes.append(morpheme)
    return morphemes


def load_morphems_iter(file='neko.txt.mecab'):
    # MeCabの出力フォーマット
    # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    for line in open(file, encoding='utf8'):
        # EOS のみの行をスキップ
        if line == 'EOS\n':
            continue
        # 要素ごとに分割
        splited = re.split('[\t,]', line.rstrip())
        # 各形態素を格納
        morpheme = {
            'surface': splited[0],
            'base'   : splited[7],
            'pos'    : splited[1],
            'pos1'   : splited[2],
        }
        yield morpheme


if __name__ == '__main__':
    gen = load_morphems_iter()
    for _ in range(10):
        print(next(gen))


'''30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

{'surface': '一', 'base': '一', 'pos': '名詞', 'pos1': '数'}
{'surface': '\u3000', 'base': '\u3000', 'pos': '記号', 'pos1': '空白'}
{'surface': '吾輩', 'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞'}
{'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'}
{'surface': '猫', 'base': '猫', 'pos': '名詞', 'pos1': '一般'}
{'surface': 'で', 'base': 'だ', 'pos': '助動詞', 'pos1': '*'}
{'surface': 'ある', 'base': 'ある', 'pos': '助動詞', 'pos1': '*'}
{'surface': '。', 'base': '。', 'pos': '記号', 'pos1': '句点'}
{'surface': '名前', 'base': '名前', 'pos': '名詞', 'pos1': '一般'}
{'surface': 'は', 'base': 'は', 'pos': '助詞', 'pos1': '係助詞'}
'''

