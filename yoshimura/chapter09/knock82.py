'''
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．

ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
'''
import random
from tqdm import tqdm
from collections import defaultdict
from sklearn.externals import joblib


vocab = defaultdict(lambda: len(vocab))
with open('context', 'w') as f:
    for line in tqdm(open('corpus81', 'r')):
        words = line.rstrip().split(' ')
        for i, word in enumerate(words):
            vocab[word]
            d = random.randint(1, 5)
            for j in range(1, d + 1):
                if i+j < len(words):
                    f.write(f'{word}\t{words[i+j]}\n')
                if i-j >= 0:
                    f.write(f'{word}\t{words[i-j]}\n')
    
joblib.dump(dict(vocab), 'vocab')