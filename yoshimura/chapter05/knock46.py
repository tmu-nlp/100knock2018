from knock41 import get_chunk_list

for line in get_chunk_list():
    for chunk in line:
        if chunk.check_pos('動詞'):
            # 述語を取得
            predicate = chunk.get_surfaces('pos', '動詞')[0]
            
            # 助動詞を取得
            avs = []
            for src in chunk.srcs:
                if len(line[src].get_surfaces('pos', '助詞')) > 0:
                    avs.append(line[src].get_surfaces('pos', '助詞').pop())
            
            # 動詞の格フレームを取得
            phrases = []
            for src in chunk.srcs:
                phrases.append(line[src].normalized_surface())

            
            if avs:
                avs = ' '.join(sorted(avs))
                phrases = ' '.join(sorted(phrases))
                print(f'{predicate}\t{avs}\t{phrases}')

# phraseが辞書順にならない