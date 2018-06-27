#!/usr/bin/env python3
# coding: utf-8
'''
69. Webアプリケーションの作成
ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．
アーティスト名，アーティストの別名，タグ等で検索条件を指定し，アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．
'''
import cgi
import pymongo
from pymongo import MongoClient
from string import Template
from html import escape

# テンプレートの読み込み
# template_search = Template(open('search_form.html').read())
template_search = Template('''
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title>あーちすと</title>
    </head>
    <body>
        <h1>アーティスト検索</h1>
        <form method="GET" action="/cgi-bin/knock69.py">
            アーティスト名: <input type="text" name="name" size="40" value=${q_name}><br />
            タグ: <input type="text" name="tag" size = "40" value=${q_tag}><br />
            <input type="submit" value="検索"/>
        </form>
        ${message}
        ${contents}
    </body>
</html>''')

# template_result = Template(open('result_form.html').read())
template_result = Template('''
<hr />
${index}件目/全${total}件<br />
[名前]: ${name}<br />
[別名]: ${aliases}<br />
[活動場所]: ${area}<br />
[タグ]: ${tags}<br />
[レーティング]: ${rating}<br />''')

# MongoDBのデータベースdbのコレクションartistにアクセス
client = MongoClient()  # MongocClient作成
db = client.database  # データベース取得
collection = db.artist  # コレクション取得

form = cgi.FieldStorage()  # クエリとして渡された値をPythonのプログラムで扱えるように変換
query = {}
q_name = ''  # 名前の入力欄の内容
q_tag = ''

if 'name' in form:
    q_name = form['name'].value
    query = {'$or': [{'name': q_name}, {'aliases.name': q_name}]}

if 'tag' in form:
    q_tag = form['tag'].value
    if len(query) > 0:
        query = {'$and': [query, {'tags_value': q_tag}]}  # 名前とタグ
    else:
        query = {'tags.value': q_tag}  # タグのみ

# 検索
contents = ''  # 検索結果の内容
total = -1  # 検索結果数
if len(query) > 0:
    results = collection.find(query)
    total = results.count()
    results.sort('rating.count', pymongo.DESCENDING)

    # 結果
    dict_template = {}
    for i, doc in enumerate(results, 1):
        dict_template['index'] = i
        dict_template['total'] = total
        dict_template['name'] = escape(doc['name'])

        if 'aliases' in doc:
            alias = '/'.join(escape(alias['name']) for alias in doc['aliases'])
            dict_template['aliases'] = alias
        else:
            dict_template['aliases'] = 'データなし'
        
        if 'area' in doc:
            dict_template['area'] = escape(doc['area'])
        else:
            dict_template['area'] = 'データなし'
        
        if 'tags' in doc:
            tags = '/'.join(escape(tag['value']) for tag in doc['tags'])
            dict_template['tags'] = tags
        else:
            dict_template['tags'] = 'データなし'
        
        if 'rating' in doc:
            dict_template['rating'] = doc['rating']['count']
        else:
            dict_template['raitng'] = 'データなし'
        
        # 結果表示部分のテンプレート適用
        contents += template_result.substitute(dict_template)

dict_template = {}
dict_template['q_name'] = escape(q_name)
dict_template['q_tag'] = escape(q_tag)
dict_template['contents'] = contents
if total == 0:
    dict_template['message'] = '検索結果なし'
else:
    dict_template['message'] = ''


# HTML全体のテンプレート適用
print(template_search.substitute(dict_template))
