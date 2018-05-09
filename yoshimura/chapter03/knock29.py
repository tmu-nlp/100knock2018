import re
import urllib.request
import urllib.parse
import json

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
                        )*
                        ([^|]*?)
                        \]\]''',re.MULTILINE | re.VERBOSE)

# {{lang|言語タグ|文字列}}
pattern_template_lang = re.compile(r'''
                        \{\{
                        (?:[^|]+)
                        \|
                        (?:[^|]+) 
                        \| 
                        ([^|]+) 
                        \}\}''',re.MULTILINE | re.VERBOSE)

# [http://www.example.org 表示文字]
pattern_external_link = re.compile(r'''           
                        \[
                        (?:.+?)
                        \s
                        (.+?)
                        \]
                        ''',re.MULTILINE | re.VERBOSE)

# <br> <br/> <ref> </ref> <ref " ">
pattern_br_ref = re.compile(r''' 
                        <
                        \/?
                        [br|ref]
                        [^>]*?
                        >
                        ''',re.MULTILINE | re.VERBOSE)

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    text = read_file.read()
    for match in pattern_template.finditer(text):
        # 強調マークアップを除去
        removed = re.sub(r'\'{2,5}','',match.group(2)) 
        # MediaWikiマークアップの除去
        removed = pattern_internal_link.sub(r'\1',removed)
        # Template:Langの除去
        removed = pattern_template_lang.sub(r'\1',removed)
        # 外部リンクの除去
        removed = pattern_external_link.sub(r'\1',removed)
        # <ref> <br>の除去
        removed = pattern_br_ref.sub('',removed)

        info_dict[match.group(1)] = removed
        

# 国旗画像の値を取得
flag_name = info_dict['国旗画像']

# リクエスト生成
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(flag_name) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

# リクエスト送信
request = urllib.request.Request(url,headers = {'User-Agent': '100knock(@yoshimura)'})
connection = urllib.request.urlopen(request)

# jsonとして受信
data = json.loads(connection.read().decode())

# print(json.dumps(data, indent = 4))

# URL取り出し
url = data['query']['pages']['-1']['imageinfo'][0]['url']

print(url)
