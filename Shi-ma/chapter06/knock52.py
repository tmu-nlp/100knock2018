from stemming.porter2 import stem

def make_word_stem(data_in):
    for word in data_in:
        word = word.strip()
        if word == '':
            yield ''
        else:
            yield word + '\t' + stem(word)

if __name__ == '__main__':
    with open('./result/knock51.txt', 'r') as data_in, open('./result/knock52.txt', 'w') as data_out:
        for word_stem in make_word_stem(data_in):
            print(word_stem, file=data_out)
