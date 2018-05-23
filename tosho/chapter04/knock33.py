import os,sys
sys.path.append(os.pardir)

from common.parsers import filter_mecab_result

def filter_neko(predicator):
    return filter_mecab_result('neko.txt.mecab', predicator)

'''
する	動詞,自立,*,*,サ変・スル,基本形,する,スル,スル
する	動詞,自立,*,*,サ変・スル,基本形,する,スル,スル
拷問	名詞,サ変接続,*,*,*,*,拷問,ゴウモン,ゴーモン
する	動詞,自立,*,*,サ変・スル,基本形,する,スル,スル
抵抗	名詞,サ変接続,*,*,*,*,抵抗,テイコウ,テイコー
'''

if __name__ == '__main__':
    from collections import defaultdict

    nouns = defaultdict(int)

    def predicator(m):
        return m.pos == '名詞' and m.pos1 == 'サ変接続'

    for m in filter_neko(predicator):
        nouns[m.base] += 1

    for v, c in nouns.items():
        print(f'{v} ({c} times)')

    print('----------')
    print(f'{len(nouns)} nouns')

