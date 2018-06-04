from knock41 import *
from knock42 import *

def find_nouns(chunk):
    for i, m in enumerate(chunk.morphs):
        if m.品詞 == '名詞':
            yield i, chunk
    for c in chunk.dep_by:
        for i,chunk in find_nouns(c):
            yield i, chunk


def noun_path(sent):
    for i, nc in find_nouns(sent):
        s = []
        while nc:
            s.append(nc.m_str('', no_punc = True))
            nc = nc.dep_on
        print(' -> '.join(s))

if __name__ == '__main__':
    sent = get_sentence(neko_sent(int(argv[1])))
    if sent:
        noun_path(sent)
