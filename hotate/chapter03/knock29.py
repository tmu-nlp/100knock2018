# -*- coding: utf-8 -*-

from knock20 import extraction
import re
import requests
import json


def basic_info(str_):
    pattern_1 = r'\{\{基礎情報.*?^(.*?)^\}\}$'
    pattern_2 = r'^\|(.*?)\s\=\s(.*?)$'
    dic = {}
    lines = re.findall(pattern_1, str_, re.MULTILINE + re.DOTALL)  # DOTALLは.を改行にもマッチさせる
    lines = re.findall(pattern_2, lines[0], re.MULTILINE)
    for line in lines:
        dic[line[0]] = line[1]
    return dic


def remove_emphasis(text):
    pattern = r'\'{2,5}'
    text = re.sub(pattern, r'', text)
    return text


def remove_link(text):
    pattern = r'\[\[([^|#\]]+?\|)*(.*?)\]\]'
    text = re.sub(pattern, r'\2', text)
    return text


def remove_all(text):
    text = re.sub(r'\[.*?\]', r'', text)
    text = re.sub(r'<.*?>', r' ', text)
    text = re.sub(r'{{([^|]+?\|){2}(.*?)}}', r'\2', text)
    return text


if __name__ == '__main__':
    s = extraction('イギリス')
    s = remove_emphasis(s)
    s = remove_link(s)
    s = remove_all(s)
    dic = basic_info(s)

    url = 'https://en.wikipedia.org/w/api.php?'
    payload = {
        'action': 'query',
        'format': 'json',
        'titles': f'File: {dic["国旗画像"]}',
        'prop': 'imageinfo',
        'iiprop': 'url'
    }
    r = requests.get(url, params=payload).text  # 文字列に変換

    print("{}".format(re.findall(r'"url":"(.*?)"', r)))
