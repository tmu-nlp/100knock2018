'''
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
'''

def main():
    INPUT_FILE = 'sentiment.txt'

    # get_top_n_words(INPUT_FILE,200)

    stop_words = StopWords()

    test_words = [
        ['of', True],
        ['mine', False],
        [',', True]
    ]

    for x, t in test_words:
        y = stop_words.is_stop_word(x)
        print(x, end='|')
        if y != t:
            print(f'incorrect (expect:{t}, actual:{y})')
        else:
            print('correct')

class StopWords(object):
    def __init__(self, file_name='stop_words.txt'):
        *self.words, = [line.split()[0] for line in open(file_name)]
    
    def is_stop_word(self, word):
        return word in self.words

def get_top_n_words(file_name, n):
    from collections import defaultdict
    from itertools import islice

    words = defaultdict(int)

    for word in [w for line in open(file_name) for w in line.rstrip().split()]:
        words[word] += 1
    
    freq_sorted = sorted(words.items(), key=lambda i:i[1], reverse=True)

    for item in islice(freq_sorted, n):
        print(*item)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')