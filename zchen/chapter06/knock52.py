from re import compile as regex
from knock50 import sentences
from knock51 import split
from stemming.porter2 import stem
from collections import Counter

c = Counter()
for sent in sentences():
    c += Counter(stem(tok) for tok in split(sent))

for tok, cnt in sorted(c.items(), key = lambda x:x[-1]):
    print('%s\t%d' % (tok, cnt))
