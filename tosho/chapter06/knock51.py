import sys, os
sys.path.append(os.pardir)
from chapter06.knock50 import load_nlp_text

def load_nlp_word(file_name='./nlp.txt'):
    for line in load_nlp_text(file_name):
        for w in line.split(' '):
            yield w
        yield ''

if __name__ == '__main__':
    import itertools

    for w in itertools.islice(load_nlp_word(), 50):
        print(w)