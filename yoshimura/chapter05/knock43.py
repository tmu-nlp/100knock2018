from knock41 import get_chunk_list

for line in get_chunk_list():
    for chunk in line:
        if chunk.dst != -1 and chunk.check_pos('名詞') and line[chunk.dst].check_pos('動詞'):
            src = chunk.normalized_surface()
            dst = line[chunk.dst].normalized_surface()
            if src != '' and dst != '':
                print(f'{src}\t{dst}')

# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．