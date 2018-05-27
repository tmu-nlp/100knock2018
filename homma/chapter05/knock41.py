class Chunk():
    """
    文節を表すクラス

    Attributes
    ----------
    morphs : List[Morph]
        文節が持つ形態素のリスト
    dst : int
        係り先文節インデックス番号
    srcs : List[int]
        係り元文節インデックス番号のリスト
    """

    def __init__(self, morphs, dst, srcs):
        """
        Parameters
        ----------
        morphs : List[Morph]
            文節が持つ形態素のリスト
        dst : int
            係り先文節インデックス番号
        srcs : List[int]
            係り元文節インデックス番号のリスト
        """
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return f"{''.join(m.surface for m in self.morphs)} {self.dst}"

    def normalized_surface(self):
        """
        記号を除いた表層形を連ねた一文節
        """
        return ''.join(m.surface for m in self.morphs if m.pos != '記号')
    
    def xy_surface(self, x_or_y: str):
        """
        名詞をXかYに置き換えて表層形を連ねた一文節。記号も除く
        """
        result = ''
        for m in self.morphs:
            if m.pos == '記号':
                continue
            elif m.pos == '名詞':
                result += x_or_y
            else:
                result += m.surface
        return result


class Morph():
    """
    形態素を表すクラス

    Attributes
    ----------
    surface : str
        表層形
    base : str
        基本形
    pos : str
        品詞
    pos1 : str
        品詞細分類1
    """

    def __init__(self, surface, base, pos, pos1):
        """
        Parameters
        ----------
        surface : str
            表層形
        base : str
            基本形
        pos : str
            品詞
        pos1 : str
            品詞細分類1
        """
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
    """
    １文ごとに係り受け解析の結果を返す
    """
    chunks = []
    srcs = []
    current_no = 0

    for line in open(file, encoding='utf8'):
        line = line.rstrip()
        # * 1 7D 2/3 -0.506012
        if line.startswith('*'):
            elements = line.split()
            current_no = int(elements[1])
            dst = int(elements[2][:-1])
            chunks.append(Chunk([], dst, srcs))
            if dst == -1:
                continue
            while len(srcs) <= dst:
                srcs.append([])
            srcs[dst].append(current_no)
        # 書生	名詞,一般,*,*,*,*,書生,ショセイ,ショセイ
        elif '\t' in line:
            surface, elements_str = line.split('\t')
            elements = elements_str.split(',')
            morph = Morph(surface, elements[6], elements[0], elements[1])
            chunks[current_no].morphs.append(morph)
        # EOS
        else:
            if len(chunks) == 0:
                continue
            yield chunks
            chunks = []
            srcs = []


def main():
    for i, chunks in enumerate(load_cabocha_iter()):
        if i != 7:
            continue
        for j, chunk in enumerate(chunks):
            print(f'{j}: {chunk}')


if __name__ == '__main__':
    main()


''' 問
41. 係り受け解析結果の読み込み（文節・係り受け）

40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

''' 実行結果
0: この 1
1: 書生というのは 7
2: 時々 4
3: 我々を 4
4: 捕えて 5
5: 煮て 6
6: 食うという 7
7: 話である。 -1
'''
