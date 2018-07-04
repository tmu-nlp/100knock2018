# coding: utf-8
import os
import subprocess
import xml.etree.ElementTree as ET

# fname = '../data/nlp.txt'
fname = '../data/out_knock50.txt'
fname_parsed = 'out_knock50.txt.xml'


def parse_nlp():
    '''nlp.txtをStanford Core NLPで解析しxmlファイルへ出力
    すでに結果ファイルが存在する場合は実行しない
    '''
    if not os.path.exists(fname_parsed):

        # StanfordCoreNLP実行、標準エラーはparse.outへ出力
        subprocess.run(
            'java -cp ./stanford-corenlp-full-2018-02-27/*'
            ' --add-modules java.se.ee'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=False,     # shellで実行
            check=True      # エラーチェックあり
        )


# nlp.txtを解析
parse_nlp()

# 解析結果のxmlをパース
root = ET.parse(fname_parsed)

# wordのみ取り出し
for word in root.iter('word'):
    print(word.text)