from knock30 import load_morphems_iter

concatenation_of_nouns = set()
count = 0
nouns = ''
for m in load_morphems_iter():
    if count and m['pos'] != '名詞':
        if count > 1:
            concatenation_of_nouns.add(nouns)
        count = 0
        nouns = ''
    elif not count and m['pos'] == '名詞' or count:
        count += 1
        nouns += m['surface']
if nouns:
    concatenation_of_nouns.add(nouns)
print(concatenation_of_nouns)


'''35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．'''
