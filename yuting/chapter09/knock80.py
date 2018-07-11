#トークンをスペースで連結してファイルに保存

import bz2
fname_input = 'enwiki-20150112-400-r100-10576.txt.bz2'    
fname_output = 'corpus80.txt'

# 1行ずつ処理
with bz2.open(fname_input, 'r') as data_file, \
        open(fname_output, 'w') as out_file:
    for line in data_file:

        # 空白で分解、前後の記号除去
        tokens = []     # 結果のトークン配列
        for chunk in line.decode().split(' '):
            token = chunk.strip().strip('.,!?;:()[]\'"')
            if len(token) > 0:
                tokens.append(token)

        # 出力
        print(*tokens, sep=' ', end='\n', file=out_file)