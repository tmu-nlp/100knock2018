from knock30 import load_morphems_iter

verb_base = set()
for m in load_morphems_iter():
    if m['pos'] == '動詞':
        verb_base.add(m['base'])
print(verb_base)


'''32. 動詞の原形
動詞の原形をすべて抽出せよ．'''
