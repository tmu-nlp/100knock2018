class Morph():

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f'表層形: {Morph.with_space_str(self.surface, 12)}'\
            f'基本形: {Morph.with_space_str(self.base, 12)}'\
            f'品詞: {Morph.with_space_str(self.pos, 10)}'\
            f'品詞細分類1: {Morph.with_space_str(self.pos1, 10)}'

    @staticmethod
    def with_space_str(string, n):
        return string + ' ' * (n - len(string) * 2)


def load_cabocha_iter(file='neko.txt.cabocha'):
    '１文ごとに形態素のリストを返す'
    morphs = []
    for line in open(file, encoding='utf8'):
        line = line.rstrip()
        if line.startswith('*'):
            pass
        elif '\t' in line:
            surface, elements_str = line.split('\t')
            elements = elements_str.split(',')
            morph = Morph(surface, elements[6], elements[0], elements[1])
            morphs.append(morph)
        elif line == 'EOS':
            if len(morphs) > 0:
                yield morphs
                morphs = []


def main():
    for i, morphs in enumerate(load_cabocha_iter()):
        if i != 2:
            continue
        for morph in morphs:
            print(morph)


if __name__ == '__main__':
    main()


''' 問
40. 係り受け解析結果の読み込み（形態素）

形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos）
，品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

cabocha -f1 < neko.txt > neko.txt.cabocha
'''

''' 実行結果
表層形: 名前        基本形: 名前        品詞: 名詞      品詞細分類1: 一般
表層形: は          基本形: は          品詞: 助詞      品詞細分類1: 係助詞
表層形: まだ        基本形: まだ        品詞: 副詞      品詞細分類1: 助詞類接続
表層形: 無い        基本形: 無い        品詞: 形容詞    品詞細分類1: 自立
表層形: 。          基本形: 。          品詞: 記号      品詞細分類1: 句点
'''
