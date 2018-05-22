from knock20 import open_england
import re


ptn = re.compile(r'\[\[Category:.*?\]\]')

print(''.join(l for l in open_england() if ptn.search(l)))


# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

# [[Category:イギリス|*]]
# [[Category:英連邦王国|*]]
# [[Category:G8加盟国]]
# [[Category:欧州連合加盟国]]
# [[Category:海洋国家]]
# [[Category:君主国]]
# [[Category:島国|くれいとふりてん]]
# [[Category:1801年に設立された州・地域]]
