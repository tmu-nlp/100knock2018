# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

file_name = 'out_knock50.txt.xml'

# 解析結果のxmlをパース
root = ET.parse(file_name)

# wordのみ取り出し
for item in root.getiterator('token'):
    if item.find('NER').text == 'PERSON':
        word = item.find('word').text
        print(word)