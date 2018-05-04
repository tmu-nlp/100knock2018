# -*- coding: utf-8 -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

surfaces = {}
bases = {}

with open('../data/neko.txt.mecab', 'r', encoding='utf-8') as f:
    for line in f:
        if line == 'EOS\n':
            pass
        else:
            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            surface = line.split('\t')[0]
            if surface in surfaces:
                surfaces[surface] += 1
            else:
                surfaces[surface] = 1

            base = line.split('\t')[1].split(',')[6] # 原型
            if base in bases:
                bases[base] += 1
            else:
                bases[base] = 1

sub_surfaces = sorted(surfaces.items(), key=lambda x: x[1], reverse=True)[0:300]
# bases10 = sorted(bases.items(), key=lambda x: x[1], reverse=True)[0:10]

data = pd.DataFrame(sub_surfaces, columns=['word', 'counts'])
data['rank'] = [i+1 for i in range(0, 300)]

f, ax = plt.subplots(figsize=(7, 7))
ax.set(xscale='log', yscale='log')
sns.regplot(x='rank', y='counts', data=data, ax=ax).set_title('The low of Zipf')
plt.show()

print(len(sub_surfaces))
print(sub_surfaces)
# print(len(bases10))
# print(bases10)

# for i in range(0, 10):
#     print()