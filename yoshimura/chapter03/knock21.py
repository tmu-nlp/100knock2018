import re

pattern = re.compile(r'^(.*\[\[Category:.*\]\].*)$', re.MULTILINE)

with open('Briten.txt','r', encoding= 'utf-8') as read_file:
    lines = read_file.read()
    result = pattern.findall(lines)    

for line in result:
    print(line)


# MULTILINEは複数行にマッチ
# re.MULTILINEでpylintのerrorがでる

