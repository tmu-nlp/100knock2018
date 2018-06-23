import xml.etree.ElementTree as ET
from itertools import islice


def output(n=None):
    root = ET.parse('knock50.txt.xml')
    for word in islice(root.iter('word'), n):
        print(word.text)

if __name__ == '__main__':
    output(10)


''' 問
53. Tokenization

Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
'''

''' 実行結果
jdk8を入れる
Bash on Ubuntu on Windowsの場合OpenJDKのバージョンが7だけなのでリポジトリを追加して8を入れる
$ sudo apt-add-repository ppa:openjdk-r/ppa
$ sudo apt update
$ sudo apt-get install openjdk-8-jdk

./corenlp.sh -ssplit.eolonly -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file ..\nlp_lines.txt -outputDirectory ..\nlp_lines.xml
java

Windows10のBoW環境でうまく行かなかったためxmlファイルを直接頂いてやる

---
Natural
language
processing
From
Wikipedia
,
the
free
encyclopedia
Natural
'''
