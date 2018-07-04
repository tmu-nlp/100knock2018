from knock41 import *
from knock42 import *

_noun_cnt = -1

def get_letter():
    global _noun_cnt
    _noun_cnt += 1
    return chr(ord('A') + _noun_cnt)

def ego(bros):
    n = len(bros)
    if n > 1:
        for i in range():
            yield bros[i], [b for j, b in enumerate(bros) if j != i]

def mark(root):
    if any(m.POS == '名詞' for m in root.morphs):
        root.letter = get_letter(), ''.join(m.surface for m in root.morphs if m.POS != '名詞')
        dep_on = root.dep_on
    for ego, others in ego(root.dep_by):
        ego.others = others
    for dep_chunk in root.dep_chunk:
        noun_path(dep_chunk)
    if len(root.dep_by) == 0:

def bottom_up(ego):
        for c for ego.dep_by:
            top_down(c)

if __name__ == '__main__':
    sent = get_sentence(neko_sent(int(argv[1])))
    if sent:
        noun_path(sent)
