# About MeCab in English
# MeCab is an general POS and Morphology Analysis tool
# It uses CRF rather than HMM and run with a specific dictionary in a language
# thus depending on that dictionary.
# The way of Basic i/o is either in its immediate running evrironment or,
# mecab INPUT_FILE -o OUTPUT_FILE.
# To split word (わかち書き) fucntion, use -O wakati option
# I am not understand other options with -O
# Bind with py3: install with mecab-python3
# switch dictionary with -d, check with -D
# mecab-ipadic-NEologd : Neologism dictionary for MeCab, a large dictionary
# Easy install for MacOS
# https://qiita.com/yuichy/items/5c8178e5cc3711386b77
# not understand: http://parame.mwj.jp/blog/0209
# user dict: https://qiita.com/hiro0217/items/cfcf801023c0b5e8b1c6

from re import compile as regex

mecab_fields = ('表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原形', '読み', '発音')
re_groups   = tuple(r'(?P<%s>[^\t,]+)' % fn for fn in mecab_fields[:8])
re_str      = ','.join(re_groups)
re_str      = re_str.replace('),(', r')\t(', 1)
re_fields   = regex(re_str)

def line_gen():
    with open('neko.tag') as fr:
        for line in fr:
            yield line.strip('\n')

if __name__ == '__main__':
    print("Using regex:", re_str)
