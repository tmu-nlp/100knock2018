from knock41 import *

def get_dep(chunk):
    deps = set()
    for c in chunk.dep_by:
        deps.add((c, chunk))
        deps |= get_dep(c)
    return deps

to_str = lambda chunk: '%s (%s)' % (chunk.func, chunk.m_str(' ', no_punc = True))

if __name__ == '__main__':
    sent = get_sentence(neko_sent(int(argv[1])))
    for i in get_dep(sent):
        print('%s\t%s' % tuple(map(to_str, i)))
