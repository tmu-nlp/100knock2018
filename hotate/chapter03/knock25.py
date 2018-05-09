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


if __name__ == '__main__':
    s = extraction('イギリス')
    for key, value in basic_info(s).items():
        print(f'{key}: {value}')
