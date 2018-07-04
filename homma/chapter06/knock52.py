import snowballstemmer
from knock51 import get_word_iter


def get_stemmed_iter(n=-1):
    stemmer = snowballstemmer.stemmer('english')
    for i, word in enumerate(get_word_iter()):
        if i == n:
            break
        yield word, stemmer.stemWord(word)


if __name__ == '__main__':
    for word, stem in get_stemmed_iter(10):
        print(f'{word}\t{stem}')


''' 問
52. ステミング

51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
'''

''' 実行結果
Natural Natur
language        languag
processing      process

From    From
Wikipedia       Wikipedia
the     the
free    free
encyclopedia    encyclopedia
'''
