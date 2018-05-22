from knock30 import load_morphems_iter

verb_surface = set()
for m in load_morphems_iter():
    if m['pos'] == '動詞':
        verb_surface.add(m['surface'])
print(verb_surface)


'''31. 動詞
動詞の表層形をすべて抽出せよ．'''
