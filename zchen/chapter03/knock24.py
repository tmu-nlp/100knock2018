from knock21 import filter_english
from re import compile as regex

# regex hates factorization!!!
# get_affix_file = regex(r'[(?P<prefix_en>File:)|(?P<prefix_jp>ファイル:)](?P<file>.+)[|\]]')
# get_affix_file = regex(r'(File:(?P<file_en>.+?)|ファイル:(?P<file_jp>.+?))\|')
get_affix_file = regex(r'File:(?P<file_en>.+?)\||ファイル:(?P<file_jp>.+?)\|')
for line in filter_english():
    result = get_affix_file.search(line)
    if result:
        fname = result.group("file_en")
        if fname:
            print("English link:", fname)
        else:
            print("Japanese link:", result.group("file_jp"))
