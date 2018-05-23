from knock30 import load_morphems_iter

sahen = set()
for m in load_morphems_iter():
    if m['pos1'] == 'サ変接続':
        sahen.add(m['surface'])
print(sahen)


'''33. サ変名詞
サ変接続の名詞をすべて抽出せよ．'''
