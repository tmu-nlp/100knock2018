import re

pattern = re.compile(r'.*\[\[Category:(.*)\]\].*', re.MULTILINE)

with open('Briten.txt','r', encoding= 'utf-8') as read_file:
    for line in read_file:
        match = re.search(pattern, line)
        if match:
            print(match.group(1))

# matchやsearchでマッチしなかった時はNoneを返す