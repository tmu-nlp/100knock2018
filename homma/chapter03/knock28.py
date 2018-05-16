from knock20 import open_england
from pprint import pprint
import regex


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

pprint(category_dic)


# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを
# 可能な限り除去し，国の基本情報を整形せよ．

# {'GDP/人': '36,727',
#  'GDP値': '2兆3162億',
#  'GDP値MER': '2兆4337億',
#  'GDP値元': '1兆5478億',
#  'GDP統計年': '2012',
#  'GDP統計年MER': '2012',
#  'GDP統計年元': '2012',
#  'GDP順位': '6',
#  'GDP順位MER': '5',
#  'ISO 3166-1': 'GB / GBR',
#  'ccTLD': '.uk / .gb',
#  '人口値': '63,181,775',
#  '人口大きさ': '1 E7',
#  '人口密度値': '246',
#  '人口統計年': '2011',
#  '人口順位': '22',
#  '位置画像': 'Location_UK_EU_Europe_001.svg',
#  '元首等氏名': 'エリザベス2世',
#  '元首等肩書': '女王',
#  '公式国名': 'United Kingdom of Great Britain and Northern Ireland',
#  '公用語': '英語（事実上）',
#  '国旗画像': 'Flag of the United Kingdom.svg',
#  '国歌': '神よ女王陛下を守り給え',
#  '国章リンク': '（国章）',
#  '国章画像': 'イギリスの国章',
#  '国際電話番号': '44',
#  '夏時間': '+1',
#  '建国形態': '建国',
#  '日本語国名': 'グレートブリテン及び北アイルランド連合王国',
#  '時間帯': '±0',
#  '最大都市': 'ロンドン',
#  '標語': 'Dieu et mon droit（フランス語:神と私の権利）',
#  '水面積率': '1.3%',
#  '注記': '',
#  '略名': 'イギリス',
#  '確立年月日1': '927年／843年',
#  '確立年月日2': '1707年',
#  '確立年月日3': '1801年',
#  '確立年月日4': '1927年',
#  '確立形態1': 'イングランド王国／スコットランド王国（両国とも1707年連合法まで）',
#  '確立形態2': 'グレートブリテン王国建国（1707年連合法）',
#  '確立形態3': 'グレートブリテン及びアイルランド連合王国建国（1800年連合法）',
#  '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更',
#  '通貨': 'UKポンド (&pound;)',
#  '通貨コード': 'GBP',
#  '面積値': '244,820',
#  '面積大きさ': '1 E11',
#  '面積順位': '76',
#  '首相等氏名': 'デーヴィッド・キャメロン',
#  '首相等肩書': '首相',
#  '首都': 'ロンドン'}
