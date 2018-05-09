import re

# [[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
pattern = re.compile(r'^\[\[(?:ファイル|File):(.+?)\|(.+)\]\]$')

with open('Briten.txt','r', encoding = 'utf-8') as read_file:
    for line in read_file:
        match = re.search(pattern, line)
        if match:
            print(match.group(1))


