import sys, os
sys.path.append(os.pardir)
from common.parsers import load_en_txt

def load_nlp_text(file_name='./nlp.txt'):
    return load_en_txt(file_name)

if __name__ == '__main__':
    import itertools

    for line in itertools.islice(load_nlp_text(), 10):
        print(line)