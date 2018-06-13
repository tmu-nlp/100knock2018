from knock41 import *
from knock42 import *

def verb_cases(chunk):
    if chunk.func == '動詞句':
        cases = []
        phrases = []
        for dep_chunk in chunk.dep_by:
            dm = dep_chunk.morphs[-1]
            if dm.POS1 == '格助詞':
                cases.append(dm.原形)
                phrases.append(to_str(dep_chunk))

        if cases:
            print('%s\t%s\t%s' % (to_str(chunk), ' '.join(cases), ' '.join(phrases)))
    for dep_chunk in chunk.dep_by:
        verb_cases(dep_chunk)

if __name__ == '__main__':
    for s in neko_sent().getchildren():
        sent = get_sentence(s)
        if sent is None:
            continue
        verb_cases(sent)
