from knock20 import open_england
from pprint import pprint
import regex
import urllib.parse
import urllib.request
import json


# 再帰的な{}の正規表現パターン
ptn1 = regex.compile(r'(?<rec>\{(?:[^{}]+|(?&rec))*\})')
# 基礎情報のフィールド名と値にマッチする正規表現パターン
ptn2 = regex.compile(r'\|(.*?) = (.*?)(?=\n(\||\}))',
                     flags=(regex.M | regex.S))

data = open_england().read()

for m in ptn1.finditer(data):
    if m.group('rec').startswith('{{基礎情報'):
        basic_info = m.group('rec')
        break

category_dic = {}
for m in ptn2.finditer(basic_info):
    value = m.group(2).replace("'''", '').replace("''", '')
    value = regex.sub(r'(\[\[(.*\|)*?(?P<d>[^|]*?)\]\])', r'\g<d>', value)
    value = regex.sub(r'(\{\{(.*\|)*?(?P<d>[^|]*?)\}\})', r'\g<d>', value)
    value = regex.sub(r'<br( *?/>|>)', '', value)
    value = regex.sub(r'<ref(.*?)(</ref>|/>)', '', value, flags=(regex.M | regex.S))
    category_dic[m.group(1)] = value


# 国旗画像の値を取得
fname_flag = category_dic['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(fname_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(
    url, headers={'User-Agent': 'tmu-nlp/100knock2018(@qavion)'})
connection = urllib.request.urlopen(request)
data = json.loads(connection.read().decode())
url = data['query']['pages']['-1']['imageinfo'][0]['url']
print(url)


# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

# https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg


