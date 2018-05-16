# -*- coding: utf-8 -*-

from knock20 import extraction
import re


def file_name(s):
    pattern = r'(?:ファイル|File):(.*?)\|'
    l = re.findall(pattern, s)
    return l


if __name__ == '__main__':
    s = extraction('イギリス')
    for l in file_name(s):
        print(l)
