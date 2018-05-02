from knock30 import query_article
import re

prog_category = re.compile(r'\[\[([^\]]+)\]\]')

if __name__ == '__main__':
    count = 0
    for article in query_article():
        text = article['text']
        for line in text.split('\n'):
            if prog_category.search(line):
                print(line)
                count += 1
    print(f'{count} lines')

'''
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''