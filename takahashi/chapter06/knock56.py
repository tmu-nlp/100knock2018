# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

file_name = 'out_knock50.txt.xml'

# 解析結果のxmlをパース
root = ET.parse(file_name)
ret = {}

# 参照情報の取得
for cor in root.iterfind('./document/coreference/coreference'):
    rep_text = cor.findtext('./mention[@representative="true"]/text')
    for mention in cor.iterfind('./mention'):
        if mention.get('representative', 'false') == 'false':
            sentence_id = int(mention.findtext('sentence'))
            start = int(mention.findtext('start'))
            end = int(mention.findtext('end'))
            if not (sentence_id, start) in ret:
                ret[(sentence_id, start)] = (end, rep_text)

# 置き換えながら表示
for sentence in root.iterfind('./document/sentences/sentence'):
    sent_id = int(sentence.get('id'))
    org_rest = 0

    for token in sentence.iterfind('./tokens/token'):
        token_id = int(token.get('id'))
        if org_rest == 0 and (sent_id, token_id) in ret:
            (end, rep_text) = ret[(sent_id, token_id)]
            print('[' + rep_text + '] (', end='')
            org_rest = end - token_id  # 置換中のtoken数の残り

        print(token.findtext('word'), end='')

        if org_rest > 0:
            org_rest -= 1
            if org_rest == 0:
                print(')', end='')

        print(' ', end='')

    print()