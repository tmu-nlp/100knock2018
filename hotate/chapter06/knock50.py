# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    with open('knock50.txt', 'w') as f:
        for line in open('nlp.txt', 'r'):
            line = line.strip('\n')
            print(re.sub(r'([.:;!?])\s([A-Z])', r'\1\n\2', line), file=f)
