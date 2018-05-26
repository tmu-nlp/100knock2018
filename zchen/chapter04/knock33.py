from knock30 import *

def extract_sa_nouns():
    verbs = set()
    for line in line_gen():
        result = re_fields.match(line)
        if result \
                and result.group('品詞') == '名詞' \
                and result.group('品詞細分類1') == 'サ変接続':
            verbs.add(result.group('原形'))
    return verbs

if __name__ == '__main__':
    print('Sa-nouns:\n', ', '.join(extract_sa_nouns()))
