import re

newline = re.compile(r'^\n', re.MULTILINE)
pattern = re.compile(r'([.;:?!]) ([A-Z])', re.MULTILINE)

txt = newline.sub('', open('nlp.txt').read())  # 改行を削除

matches = pattern.finditer(txt)
for match in matches:
    txt = pattern.sub(f'{match.group(1)}\n{match.group(2)}', txt, count=1)
print(txt)
