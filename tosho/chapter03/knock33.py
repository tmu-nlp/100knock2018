from knock30 import query_article
import re

prog_category = re.compile(r'==([=]*) ([^\s]+) ([=]*)==')

if __name__ == '__main__':
    count = 0
    for article in query_article():
        text = article['text']
        for m in prog_category.findall(text):
            count += 1
            level = len(m[0]) + 1
            header = m[1]
            print(f'{header} : {level}')
    print(f'{count} headers')

'''
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''