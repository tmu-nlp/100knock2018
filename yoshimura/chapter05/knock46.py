from knock41 import get_chunk_list

for line in get_chunk_list():
    for chunk in line:
        if chunk.check_pos('動詞'):
            # 述語を取得
            predicate = chunk.get_surfaces('pos', '動詞')[0]

            # 助動詞と動詞の格フレームをを取得
            avs = []
            phrases = []
            for src in chunk.srcs:
                phrases.append(line[src].normalized_surface())
                if len(line[src].get_surfaces('pos', '助詞')) > 0:
                    avs.append(line[src].get_surfaces('pos', '助詞').pop())
            
            if avs:
                avs = ' '.join(avs)
                phrases = ' '.join(phrases)
                print(f'{predicate}\t{avs}\t{phrases}')
