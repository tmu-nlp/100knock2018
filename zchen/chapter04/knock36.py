from knock30 import *
from collections import defaultdict as dd

def word_freq():
    cnt = dd(int)
    for line in line_gen():
        split_at = line.find('\t')
        if split_at > 0:
            cnt[ line[:split_at] ] += 1
    return cnt

if __name__ == '__main__':
    freq = sorted(word_freq().items(), key = lambda x:-x[1])

    print('Top 10: (check freq.csv file)')
    for i in range(10):
        print(freq[i])

    with open('freq.csv', 'w') as fw:
        fw.write('word,count\n')
        for tp in freq:
            fw.write('%s,%d\n' % tp)
