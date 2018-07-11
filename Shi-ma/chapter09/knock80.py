import re

if __name__ == '__main__':
    token_list = list()
    pettern = re.compile(r'^[.,!?;:()\[\]\'"]+|[.,!?;:()\[\]\'"]+$')

    with open('result/knock80_result.txt', 'w') as data_out:
        for line in open('../data/enwiki-20150112-400-r100-10576.txt', 'r'):
            sentence = list()
            for token in line.strip().split():
                if pettern.sub('', token) == '':
                    continue
                sentence.append(pettern.sub('', token))
            print(' '.join(sentence), file=data_out)
