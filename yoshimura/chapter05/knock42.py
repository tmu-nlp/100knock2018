from knock41 import get_chunk_list

for line in get_chunk_list():
    for chunk in line:
        if chunk.dst != -1:
            src = chunk.normalized_surface()
            dst = line[chunk.dst].normalized_surface()
            if src != '' and dst != '':
                print(f'{src}\t{dst}')


# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．