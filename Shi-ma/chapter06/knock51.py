def split_sentence(data_in):
    for line in data_in:
        for word in line.strip().split():
            yield word
        yield ''

if __name__ == '__main__':
    with open('./result/knock50.txt', 'r') as data_in, open('./result/knock51.txt', 'w') as data_out:
        for word in split_sentence(data_in):
            print(word, file=data_out)
