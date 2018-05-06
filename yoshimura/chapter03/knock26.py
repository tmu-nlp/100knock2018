import re

pattern = re.compile(r'^\|(.+)\s=(.+)$')

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    for line in read_file:
        match = re.search(pattern, line)
        if match:
            # 強調マークアップを除去
            removed = re.sub(r'\'{2,5}','',match.group(2)) 
            info_dict[match.group(1)] = removed


for key, value in info_dict.items():
    print(key, value)


