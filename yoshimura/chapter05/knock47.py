from knock41 import get_chunk_list

for line in get_chunk_list():
    for chunk in line:
        if chunk.check_pos('動詞'):

            # 係り元の「サ変接続名詞+を（助詞）」で構成される文節を取得
            sahen_wo = ''
            for src in chunk.srcs:
                sahen_wo = line[src].get_sahen_wo()
            
            if sahen_wo:
                # 述語を取得
                predicate = sahen_wo + chunk.get_surfaces('pos', '動詞')[0]

                # この文節にかかる'を'以外の助動詞を取得
                avs = []
                for src in chunk.srcs:
                    if len(line[src].get_surfaces('pos', '助詞')) > 0:
                        av = line[src].get_surfaces('pos', '助詞').pop()
                        if av != 'を':
                            avs.append(av)
            
                # この文節にかかる「サ変接続名詞+を（助詞）」以外の動詞の格フレームを取得
                phrases = []
                for src in chunk.srcs:
                    phrase = line[src].normalized_surface()
                    if phrase != sahen_wo:
                        phrases.append(line[src].normalized_surface())

                avs = ' '.join(sorted(avs))
                phrases = ' '.join(sorted(phrases))
                print(f'{predicate}\t{avs}\t{phrases}')

# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）