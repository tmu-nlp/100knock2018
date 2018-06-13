from knock20 import open_england
import re


# 説明文込み
# ptn = re.compile(r'\[\[(ファイル|File):(.*)\]\]')

# リンクのみ
ptn = re.compile(r'\[\[(ファイル|File):(.*)\|thumb.*\]\]')

print('\n'.join(ptn.search(l).group(2) for l in open_england() if ptn.search(l)))


# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
