from re import compile as regex

sentence_delim = regex(r'([.;:?!])\s+([A-Z])')

def sentences():
    with open('nlp.txt') as fr:
        for line in fr:
            line = sentence_delim.sub(r'\1\n\2', line)
            for sent in line.split('\n'):
                if sent:
                    yield sent

if __name__ == '__main__':
    for s in sentences():
        print(s)
