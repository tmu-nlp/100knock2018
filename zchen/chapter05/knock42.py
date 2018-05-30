from knock41 import *

def show_dep(chunk):
    h = chunk.head
    for c in chunk.dep_by:
        d = c.head
        if len(c.dep_by) == 0:
            d += ' (%s)' % c.m_str().replace('|', ' ')
        print(h, '<-', d)
        show_dep(c)

if __name__ == '__main__':
    sents = get_sentence()
    show_dep(sents[7])
