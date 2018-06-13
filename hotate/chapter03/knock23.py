# -*- coding: utf-8 -*-

from knock20 import extraction
import re


def section(s):
    pattern = r'^(=+)(.*?)=+$'
    find = re.findall(pattern, s, flags=re.MULTILINE)  # ^を複数行に適用させる
    return {line[1]: len(line[0]) - 1 for line in find}


if __name__ == '__main__':
    str_ = extraction('イギリス')
    print(section(str_))
