import re

# |フィールド名 = 値
pattern_template = re.compile(r'''
                        ^
                        \|
                        (.+?)
                        \s
                        =
                        \s
                        (.+?)
                        (?=
                            \n
                            (\||\})
                        )
                        ''',re.MULTILINE | re.DOTALL | re.VERBOSE)

# [[記事名]]	
# [[記事名|表示文字]]	
# [[記事名#節名|表示文字]] 
pattern_internal_link = re.compile(r'''
                        \[\[
                        (?:
                            [^|]*?
                            \|
                        )*?
                        ([^|]*?)
                        \]\]''',re.VERBOSE | re.MULTILINE)

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    text = read_file.read()
    for match in pattern_template.finditer(text):
        # 強調マークアップ除去
        removed = re.sub(r'\'{2,5}','',match.group(2)) 
        # MediaWikiマークアップの除去
        removed = pattern_internal_link.sub(r'\1',removed)

        info_dict[match.group(1)] = removed

for key, value in info_dict.items():
    print(key, value)


#Briten.txtに正規表現をかけると最長マッチになるのはなぜ