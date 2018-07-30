# coding: utf-8

from string import Template
from html import escape
import cgi
import cgitb
import pymongo

max_view_count = 20     # 最大結果表示数

# HTML全体のテンプレート
template_html = Template('''
<html>
    <head>
        <title>knock69 アーティスト検索Webアプリ</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <form method="GET" action="/cgi-bin/main.py">
            名前、別名：<input type="text" name="name" value="$clue_name" size="20"/><br />
            タグ：<input type="text" name="tag" value="$clue_tag" size="20"/><br />
            <input type="submit" value="検索"/>
        </form>
        $message
        $contents
    </body>
</html>
''')

# 結果表示部分(template_htmlの$contents部分)のテンプレート
template_result = Template('''
        <hr />
        ($index件目/全$total件)<br />
        〔名前〕$name<br />
        〔別名〕$aliases<br />
        〔活動場所〕$area<br />
        〔タグ〕$tags<br />
        〔レーティング〕$rating<br />
''')

# MongoDBのデータベースにアクセス
client = pymongo.MongoClient()
db = client.db_knock64
collection = db.collection_knock64

# 条件を作成
form = cgi.FieldStorage()
clue = {}
clue_name = ''      # 名前の入力欄の内容
clue_tag = ''       # タグの入力欄の内容

if 'name' in form:
    clue_name = form['name'].value
    clue = {'$or': [{'name': clue_name}, {'aliases.name': clue_name}]}

if 'tag' in form:
    clue_tag = form['tag'].value
    if len(clue) > 0:
        clue = {'$and': [clue, {'tags.value': clue_tag}]}   # 名前とタグの組み合わせ
    else:
        clue = {'tags.value': clue_tag}                     # タグのみ

# 検索、ソート
contents = ''       # 検索結果部分の出力内容
total = -1          # 結果件数、未検索時は-1
if len(clue) > 0:

    results = collection.find(clue)
    results.sort('rating.count', pymongo.DESCENDING)
    total = results.count()

    # 結果を整形
    dict_template = {}
    for i, doc in enumerate(results[0:max_view_count], start=1):

        # 結果表示部分のテンプレート用辞書に内容をセット
        dict_template['index'] = i
        dict_template['total'] = total
        dict_template['name'] = escape(doc['name'])

        if 'aliases' in doc:
            dict_template['aliases'] = \
                ','.join(escape(alias['name']) for alias in doc['aliases'])
        else:
            dict_template['aliases'] = '(データなし)'

        if 'area' in doc:
            dict_template['area'] = escape(doc['area'])
        else:
            dict_template['area'] = '(データなし)'

        if 'tags' in doc:
            dict_template['tags'] = \
                ','.join(escape(tag['value']) for tag in doc['tags'])
        else:
            dict_template['tags'] = '(データなし)'

        if 'rating' in doc:
            dict_template['rating'] = doc['rating']['count']
        else:
            dict_template['rating'] = '(データなし)'

        # 結果表示部分のテンプレート適用
        contents += template_result.substitute(dict_template)

# HTML全体のテンプレート用辞書に内容をセット
dict_template = {}
dict_template['clue_name'] = escape(clue_name)
dict_template['clue_tag'] = escape(clue_tag)
dict_template['contents'] = contents

if total > max_view_count:
    dict_template['message'] = f'結果が多いためレーティングの高い順で{max_view_count}件を表示しています'
elif total == -1:
    dict_template['message'] = '検索条件を入力してください'
elif total == 0:
    dict_template['message'] = '該当するアーティストは見つかりませんでした'
else:
    dict_template['message'] = ''

# HTML全体のテンプレート適用、出力
print(template_html.substitute(dict_template))


''' 問
69. Webアプリケーションの作成

ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．
アーティスト名，アーティストの別名，タグ等で検索条件を指定し，
アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．
'''

''' 実行結果
このファイルを cgi-bin/main.py として配置
python -m http.server --cgi 8000
ブラウザで localhost:8000/cgi-bin/main.py にアクセス
'''
