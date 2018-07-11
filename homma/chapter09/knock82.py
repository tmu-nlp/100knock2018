import random
from tqdm import tqdm


def get_contexts(words, i):
    'ランダムな文脈幅d={1,2,3,4,5}でi番目の単語の文脈を取得する'
    clamp = lambda x: max(0, min(len(words), x))
    d = random.randint(1, 5)
    left = words[clamp(i - d):i]
    right = words[clamp(i + 1):clamp(i + d + 1)]
    return ' '.join(left + right)


def main():
    with open('knock82_out', 'w', encoding='utf8') as f:
        buffer = []
        for j, line in enumerate(tqdm(open('knock81_out', encoding='utf8'))):
            if j % 500 == 0:
                f.writelines(buffer)
                buffer = []
            words = line.strip().split()
            for i, word in enumerate(words):
                buffer.append(f'{word}\t{get_contexts(words, i)}\n')
        f.writelines(buffer)

if __name__ == '__main__':
    main()


''' 問
82. 文脈の抽出

81で作成したコーパス中に出現するすべての単語tに関して，
単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

* ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
* 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
'''

''' 実行結果
$ head knock82_out

Anarchism
Anarchism       is
is      Anarchism a political
a       Anarchism is political philosophy that advocates stateless
political       Anarchism is a philosophy that advocates stateless societies
philosophy      is a political that advocates stateless
that    political philosophy advocates stateless
advocates       a political philosophy that stateless societies often defined
stateless       political philosophy that advocates societies often defined as
societies       stateless often
'''
