import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

# coreference部分を読み取り、代表参照表現(representative mention)と参照表現(mention)を得る
replace = {}  # {(sentence id, start token id); end_id srepresentative mention }
for coreference in tree.iterfind('./document/coreference/coreference'):
    # 代表参照表現を取得
    rep_mention = coreference.findtext('./mention[@representative="true"]/text')
    for mention in coreference.iterfind('./mention'):
        # 参照表現から置換辞書を作成
        if mention.get('representative', 'false') == 'false':
            sentence_id = int(mention.findtext('sentence'))
            start_id = int(mention.findtext('start'))
            end_id = int(mention.findtext('end'))
            replace[(sentence_id, start_id)] = (end_id, rep_mention)

# 文を表示していく　置換する部分があったら置換
for sentence in tree.iterfind('./document/sentences/sentence'):
    sentence_id = int(sentence.get('id'))
    num_left = 0

    for token in sentence.iterfind('./tokens/token'):
        token_id = int(token.get('id'))

        # 置換対象の場合
        if (sentence_id, token_id) in replace:
            # 終了位置と代表表現の抽出
            end, rep_mention = replace[(sentence_id, token_id)]
            # 代表表現を表示
            print(f'[{rep_mention}]', end='')
            print('(', end='')  # (とwordを表示
            num_left = end - token_id  # 残りの置換するtoken数
        
        print(token.findtext('word'), end='')
        
        num_left -= 1
        # 参照表現を全部表示したらカッコで閉じる
        if num_left == 0:
            print(')', end='')
        print(' ', end='')
    
    print('')






