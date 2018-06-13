from knock20 import query_article
import re

# [[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
# [[File:Wikipedia-logo-v2-ja.png]]
prog_category = re.compile(r'\[\[(File|ファイル):([^\]\|]+)')

if __name__ == '__main__':
    count = 0
    for article in query_article():
        text = article['text']
        for m in prog_category.findall(text):
            count += 1
            print(m[1])
    print(f'{count} files')

'''
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''