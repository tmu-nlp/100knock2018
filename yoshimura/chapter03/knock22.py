import re

# [[Category:ヘルプ|はやみひよう]]
pattern = re.compile(r'^\[\[Category:(.+?)(?:\|.+)?\]\]$')

with open('Briten.txt','r', encoding= 'utf-8') as read_file:
    for line in read_file:
        match = pattern.search(line)
        if match:
            print(match.group(1))

# (?:)でキャプチャ対象外