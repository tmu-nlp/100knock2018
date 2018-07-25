'''
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
'''
from collections import defaultdict

analogy = defaultdict(list)
for line in open('questions-words.txt'):
    if line[0] == ':':
        start_section = line.rstrip('\n')[2:]
    else:
        analogy[start_section].append(line.rstrip('\n'))

with open('family', 'w') as f:
    for line in analogy['family']:
        f.write(line + '\n')