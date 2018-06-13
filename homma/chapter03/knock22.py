from knock20 import open_england
import re


ptn = re.compile(r'\[\[Category:(.*)\]\]')

print('\n'.join(ptn.search(l).group(1) for l in open_england() if ptn.search(l)))


# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

# イギリス|*
# 英連邦王国|*
# G8加盟国
# 欧州連合加盟国
# 海洋国家
# 君主国
# 島国|くれいとふりてん
# 1801年に設立された州・地域
