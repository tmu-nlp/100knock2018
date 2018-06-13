from knock41 import *
from knock42 import *

def verb_cases(chunk):
    if chunk.func == '動詞句' and chunk.dep_by:
        cases = []
        phrases = []
        sa_wo_chunk = chunk.dep_by[-1]
        found = False

        if len(sa_wo_chunk.morphs) >= 2:
            sa, wo = sa_wo_chunk.morphs[-2:]
            if sa.品詞 == '名詞' and sa.POS1 == 'サ変接続' \
                    and wo.POS1 == '格助詞' and wo.原形 == 'を':
                found = True
                for dep_chunk in chunk.dep_by:
                    cases.append(dep_chunk.morphs[-1].原形)
                    phrases.append(to_str(dep_chunk))

        if found:
            print('%s\t%s\t%s' % (to_str(chunk), ' '.join(cases), ' '.join(phrases)))
    for dep_chunk in chunk.dep_by:
        verb_cases(dep_chunk)

if __name__ == '__main__':
    for i, s in enumerate(neko_sent().getchildren()):
        sent = get_sentence(s)
        if sent is None:
            continue
        verb_cases(sent)
