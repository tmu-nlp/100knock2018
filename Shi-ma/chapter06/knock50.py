import re

def split_sentences(data_in):
    pettern = re.compile(r'(?<=[.;:?!])\s(?=[A-Z])')
    for line in data_in:
        yield pettern.sub('\n', line.strip())



if __name__ == '__main__':
    with open('../data/nlp.txt', 'r') as data_in, open('./result/knock50.txt', 'w') as data_out:
        for sentence in split_sentences(data_in):
            if sentence == '':
                continue
            print(sentence, file=data_out)
