# -*- coding: utf-8 -*-
import re



def nlp_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        pattern = re.compile(r'''(^.*?[.|;|:|?|!])\s([A-Z].*)''', re.MULTILINE+re.VERBOSE+re.DOTALL)
        for line in f:
            line = line.strip()
            while len(line) > 0:
                match = pattern.match(line)
                if match:
                    yield match.group(1)
                    line = match.group(2)
                else:
                    yield line
                    line = ''

if __name__ == '__main__':
    file_name = '../data/nlp.txt'
    with open('out_knock50.txt', 'w', encoding='utf-8') as f:
        for line in nlp_lines(file_name):
            print(line, file=f)