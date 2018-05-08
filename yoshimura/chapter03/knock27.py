import re

pattern = re.compile(r'''
                        ^
                        \|
                        (.+)
                        \s
                        =
                        (.+)
                        $
                        ''',re.VERBOSE)

# [[記事名]]	
# [[記事名|表示文字]]	
# [[記事名#節名|表示文字]] 
pattern2 = re.compile(r'''
                        \[\[
                        (?:
                            [^|]*?
                            \|
                        )*?
                        ([^|]*?)
                        \]\]''',re.VERBOSE)

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    for line in read_file:
        match = re.search(pattern, line)
        if match:
            # 強調マークアップを除去
            removed = re.sub(r'\'{2,5}','',match.group(2)) 
            # MediaWikiマークアップの除去
            removed = pattern2.sub(r'\1',removed)

            info_dict[match.group(1)] = removed

for key, value in info_dict.items():
    print(key, value)


#Briten.txtに正規表現をかけると最長マッチになるのはなぜ