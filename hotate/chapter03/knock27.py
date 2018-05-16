# -*- coding: utf-8 -*-

from knock20 import extraction
import re


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


if __name__ == '__main__':
    s = extraction('イギリス')
    s = remove_emphasis(s)
    s = remove_link(s)
    for key, value in basic_info(s).items():
        print(f'{key}: {value}')
