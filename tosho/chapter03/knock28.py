from knock20 import query_article
import regex as re

pattern = r'(?<rec>{{(?:[^{}]+|(?&rec))*}})'
prog = re.compile(pattern)

def parse_basic_info(m):
    info = {}
    key = ''
    for item in m.strip('{}\n').split('\n'):
        # 新しい情報の場合
        if item[0] == '|':
            m = re.match(r'\|([\w\s]+)=(.*)', item)
            if m:
                key = m[1]
                value = m[2]
                info[key] = sanitize(value)
        # 情報の値が２行以上の場合
        elif key != '':
            info[key] += '\n' + sanitize(item)
        # 系列の先頭が | で始まらない場合（基本的にないので無視する）
        else:
            pass
    return info

def sanitize(text):
    '''
    wikiのテキストデータを整理する
    '''
    text = remove_em(text)
    text = remove_internal_link(text)
    text = remove_stub(text)
    text = remove_external_link(text)
    text = remove_comment(text)
    text = remove_br(text)
    text = remove_ref(text)
    return text

def remove_em(text):
    '''
    強調表示を削除する
    '''
    text = re.sub(r'[\']{2,5}([^\']+)[\']{2,5}', r'\1', text)
    return text

def remove_internal_link(text):
    '''
    内部リンクを削除する
    https://regex101.com/r/Y1BDbs/2/
    '''
    text = re.sub(r'\[\[([^\[\]\|]+\|)*([^\[\]]+)\]\]', r'\2', text)
    return text

def remove_stub(text):
    '''
    スタブを削除する
    https://regex101.com/r/28fxJN/1
    '''
    text = re.sub(r'\{\{([^\{\}\|]+\|)*([^\{\}]+)\}\}', r'\2', text)
    return text

def remove_external_link(text):
    '''
    外部リンクを削除する
    https://regex101.com/r/93DmKj/1
    変換例：
    [http://www.example.org] => ''
    [http://www.example.org text] => 'text'
    http://www.example.org => http://www.example.org
    '''
    text = re.sub(r'\[([^\[\]\s]+\s)?([^\[\]]+)\]', r'\2', text)
    return text

def remove_comment(text):
    '''
    コメントを削除する
    https://regex101.com/r/EtmUy2/1
    参考:
    https://stackoverflow.com/questions/1084741/regexp-to-strip-html-comments
    '''
    text = re.sub(r'<!--(.*?)-->', r'', text)
    return text

def remove_br(text):
    '''
    <br /> / <br> を削除する
    '''
    text = re.sub(r'<br(.*?)>', ' ', text)
    return text

def remove_ref(text):
    '''
    <ref>text</ref> => ' text'
    <ref /> => ''
    https://regex101.com/r/btERYK/1
    '''
    text = re.sub(r'<ref[^>]*>', r' ', text)
    text = re.sub(r'</ref>', r'', text)
    return text

if __name__ == '__main__':
    count = 0
    for article in query_article():
        text = article['text']
        for m in prog.findall(text):
            if '基礎情報' not in m:
                continue
            info = parse_basic_info(m)
            count += 1
            for key, value in info.items():
                print(f'{key} | {value}')
    print(f'{count} templates')

'''
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''
# {{基礎情報 国
# |略名 =インド
# |日本語国名 =インド共和国
# |公式国名 ={{lang|hi|'''भारत गणराज्य'''}} {{smaller|（ヒンディー語）}}<br/>{{lang|en|'''Republic of India'''}} {{smaller|（英語）}}
# |国旗画像 =Flag_of_India.svg
# |国章画像 =[[ファイル:Emblem of India.svg|80px|インドの国章]]
# |国章リンク =（[[インドの国章|国章]]）
# |標語 ={{lang|sa|'''सत्यमेव जयते'''}}<br/>ラテン文字転写: \"satyam eva jayate\"<br/>（サンスクリット語: まさに真理は自ずと勝利する）
# |位置画像 =India (orthographic projection).svg
# |公用語 =[[ヒンディー語]]（連邦公用語）<br/>[[英語]]（連邦準公用語）<br/>その他[[#インドの公用語|複数の各州公用語]]
# |首都 =[[ニューデリー]]<ref>[http://www.mofa.go.jp/mofaj/area/india/data.html 各国地域情勢 インド] 外務省(Ministry of Foreign Affairs of Japan)</ref>
# |最大都市 =[[ムンバイ]]
# |元首等肩書 =[[インドの大統領|大統領]]
# |元首等氏名 =[[プラナブ・ムカルジー]]
# |首相等肩書 =[[インドの歴代首相|首相]]
# |首相等氏名 =[[ナレンドラ・モディ]]
# |面積順位 =7
# |面積大きさ =1 E12
# |面積値 =3,287,590
# |水面積率 =9.6%
# |人口統計年 =2011
# |人口順位 =2
# |人口大きさ =1 E9
# |人口値 =12億1000万
# |人口密度値 =368
# |GDP統計年元 =2013
# |GDP値元 =110兆4,768億<ref name=\"economy\">IMF Data and Statistics 2014年5月19日閲覧（[http://www.imf.org/external/pubs/ft/weo/2013/01/weodata/weorept.aspx?pr.x=38&pr.y=13&sy=2011&ey=2018&scsm=1&ssd=1&sort=country&ds=.&br=1&c=534&s=NGDP_RPCH%2CNGDPD%2CNGDPDPC%2CPPPGDP%2CPPPPC&grp=0&a=]）</ref>
# |GDP統計年MER =2013
# |GDP順位MER =10
# |GDP値MER =1兆9,728億<ref name=\"economy\" />
# |GDP統計年 =2013
# |GDP順位 =3
# |GDP値 =5兆3,020億<ref name=\"economy\" />
# |GDP/人 =4,060<ref name=\"economy\" />
# |建国形態 =[[独立]]<br/>&nbsp;-&nbsp;日付
# |建国年月日 =[[イギリス]]より<br/>[[1947年]][[8月15日]]
# |通貨 =[[インド・ルピー]]
# |通貨コード =INR
# |時間帯 =(+5:30)
# |夏時間 =なし
# |国歌 =[[ジャナ・ガナ・マナ]]
# |ISO 3166-1 = IN / IND
# |ccTLD =[[.in]]
# |国際電話番号 =91
# |注記 =
# }}