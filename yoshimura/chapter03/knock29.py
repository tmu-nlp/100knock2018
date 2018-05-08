import re
import urllib.request
import urllib.parse
import json

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
                        )*
                        ([^|]*?)
                        \]\]''',re.VERBOSE)

# {{lang|言語タグ|文字列}}
pattern3 = re.compile(r'''
                        \{\{
                        (?:[^|]+)
                        \|
                        (?:[^|]+) 
                        \| 
                        ([^|]+) 
                        \}\}''',re.VERBOSE)

# [http://www.example.org 表示文字]
pattern4 = re.compile(r'''           
                        \[
                        (?:.+?)
                        \s
                        (.+?)
                        \]
                        ''',re.VERBOSE)

# <br> <br/> <ref> </ref> <ref " ">
pattern5 = re.compile(r''' 
                        <
                        \/?
                        [br|ref]
                        [^>]*?
                        >
                        ''',re.VERBOSE)

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    for line in read_file:
        match = re.search(pattern, line)
        if match:
            # 強調マークアップを除去
            removed = re.sub(r'\'{2,5}','',match.group(2)) 
            # MediaWikiマークアップの除去
            removed = pattern2.sub(r'\1',removed)
            # Template:Langの除去
            removed = pattern3.sub(r'\1',removed)
            # 外部リンクの除去
            removed = pattern4.sub(r'\1',removed)
            # <ref> <br>の除去
            removed = pattern5.sub('',removed)

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
