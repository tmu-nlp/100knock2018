def main():
    data_path = 'questions-words.txt'
    out_path = 'knock91_family'

    with open(out_path, 'w', encoding='utf8') as f:
        is_target = False
        lines = []
        for line in open(data_path, encoding='utf8'):
            if line.rstrip() == ': family':
                is_target = True
                continue
            if not is_target:
                continue
            if line.startswith(': '):
                break
            lines.append(line)
        f.writelines(lines)


if __name__ == '__main__':
    main()


''' 問
91. アナロジーデータの準備

単語アナロジーの評価データをダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，
"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
'''

''' 実行結果
$ head knock91_family
boy girl brother sister
boy girl brothers sisters
boy girl dad mom
boy girl father mother
boy girl grandfather grandmother
boy girl grandpa grandma
boy girl grandson granddaughter
boy girl groom bride
boy girl he she
boy girl his her
'''
