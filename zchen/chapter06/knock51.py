from re import compile as regex
from knock50 import sentences

expand = regex(r'([.,:?!]|[A-Z]\w+|(\w\.){2,})')
invisible = regex(r'[\s\b]+')

def split(line):
    line = expand.sub(r' \1 ', line) # or src_obj.index
    return tuple(i for i in invisible.split(line) if len(i))

if __name__ == '__main__':
    for sent in sentences():
        for tok in split(sent):
            print(tok)
