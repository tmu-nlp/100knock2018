from knock30 import query_article
import re

prog_category = re.compile(r'\[\[Category:([^\]]+)\]\]')

if __name__ == '__main__':
    count = 0
    for article in query_article():
        text = article['text']
        matches = prog_category.findall(text)
        for m in matches:
            count += 1
            print(m)
    print(f'{count} matches')

'''
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''