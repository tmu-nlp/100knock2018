import re

pattern = re.compile(r'^\|(.+)\s=(.+)$')

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    for line in read_file:
        match = re.search(pattern, line)
        if match:
            # 強調マークアップを除去
            removed = re.sub(r'\'{2,5}','',match.group(2)) 
            # MediaWikiマークアップの除去
            for m in re.finditer(r'\[\[(.+?)\]\]',removed):
                match1 = re.search(r'\|(.+)',m.group(1))
                if match1:
                    removed = re.sub(m.group(),match1.group(1),removed)
                else:
                    removed = re.sub(m.group(),m.group(1),removed)

            info_dict[match.group(1)] = removed


for key, value in info_dict.items():
    print(key, value)