'''
wc
    5331  111628  612290 rt-polarity.neg
    5331  112445  626168 rt-polarity.pos

'''

from random import shuffle

POS_FILE='rt-polarity.pos'
NEG_FILE='rt-polarity.neg'
OUTPUT='sentiment.txt'

def main():
    sentences = []
    # https://stackoverflow.com/questions/30996289/utf8-codec-cant-decode-byte-0xf3
    for line in open(POS_FILE, encoding='latin-1'):
        sentences.append(f'+1 {line}')
    for line in open(NEG_FILE, encoding='latin-1'):
        sentences.append(f'-1 {line}')
    shuffle(sentences)
    
    # print some samples
    print(*sentences[:5])

    with open(OUTPUT, 'w') as o:
        o.writelines(sentences)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')