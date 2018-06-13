import re

newline = re.compile(r'\n', re.MULTILINE)  # 改行
space = re.compile(r' ', re.MULTILINE)  # 空白

txt = newline.sub('\n\n', open('result50').read())
txt = space.sub('\n', txt)
txt = re.sub(r'\n{3}', '', txt)  # 余分な改行を削除
print(txt)
