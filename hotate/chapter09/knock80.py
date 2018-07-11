# -*- coding: utf-8 -*-


def remove_(line):
    words = line.strip().split()
    rem = []
    for word in words:
        word = word.strip(r'.,!?;:()[]\'\"')
        if len(word) > 0:
            rem.append(word)
    return ' '.join(rem)


if __name__ == '__main__':
    with open('knock_80_100', 'w') as f:
        for i, line in enumerate(open('enwiki-20150112-400-r100-10576.txt', 'r')):
            if i % 100000 == 0:
                print(i)
            print(remove_(line), file=f)
