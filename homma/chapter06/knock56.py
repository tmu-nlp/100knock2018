import xml.etree.ElementTree as ET
from collections import defaultdict
from itertools import islice


def main(n=None):
    '''n文だけ，参照表現を代表参照表現に置換しつつ表示する'''
    root = ET.parse('knock50.txt.xml')

    replace = {}
    # 置換のための辞書
    # {(sentence_id, start_id): end_id, repre_mention}
    for coreference in root.iterfind('.//coreference/coreference'):
        for mention in coreference.iterfind('./mention'):
            if 'representative' in mention.attrib and mention.attrib['representative']:
                # 代表参照表現を取得
                repre_mention = mention.findtext('text')
            else:
                # 参照表現の位置と代表参照を辞書に保存
                sentence_id = int(mention.findtext('sentence'))
                start_id = int(mention.findtext('start'))
                end_id = int(mention.findtext('end'))
                replace[sentence_id, start_id] = (end_id, repre_mention)

    # 置換しながら文を表示
    close_brackets = defaultdict(int)
    # 閉じカッコを出力するための辞書
    # {(sentence_id, token_id): 回数}
    for sentence in islice(root.iterfind('./document/sentences/sentence'), n):
        sentence_id = int(sentence.get('id'))
        for token in sentence.iterfind('./tokens/token'):
            token_id = int(token.get('id'))
            # 置換
            if (sentence_id, token_id) in replace:
                end_id, repre_mention = replace[sentence_id, token_id]
                close_brackets[sentence_id, end_id - 1] += 1
                print(f'「{repre_mention}（', end='')
            print(token.findtext('word'),
                '）」' * close_brackets[sentence_id, token_id], sep='', end=' ')
        print('')


if __name__ == '__main__':
    main(10)


''' 問
56. 共参照解析

Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）
を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，
「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
'''

''' 実行結果
Natural language processing
From Wikipedia , 「Wikipedia（the free encyclopedia）」
Natural language processing -LRB- NLP -RRB- is a field of computer science , artificial intelligence , and linguistics concerned with the interactions between computers and human -LRB- natural -RRB- languages .
As such , NLP is related to the area of humani-computer interaction .
Many challenges in NLP involve natural language understanding , that is , enabling 「computers（computers）」 to derive meaning from human or natural language input , and others involve natural language generation .
History
The history of NLP generally starts in the 1950s , although work can be found from earlier periods .
In 1950 , Alan Turing published an article titled `` Computing Machinery and Intelligence '' which proposed what is now called the 「Alan Turing（Turing）」 test as a criterion of intelligence .
The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English .
The authors claimed that within three or five years , 「a solved problem（machine translation）」 would be a solved problem .
'''
