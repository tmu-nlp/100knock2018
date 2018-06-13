from collections import defaultdict
    
def extract_sahen(chunks):
    relations = defaultdict(list)
    for chunk in chunks:
        if chunk.dst is None:
            continue
        
        # 名詞節を検査
        noun = chunk.morph_of_pos('名詞', 'サ変接続')
        particle = chunk.morph_of_pos('助詞')
        
        if len(chunk.morphs) != 2 or \
            noun is None or \
            particle is None or \
            particle.base != 'を':
            continue

        # 係り先の動詞節を検査
        dst_chunk = chunks[chunk.dst]
        verb = dst_chunk.morph_of_pos('動詞')
        if verb is None:
            continue
        
        # 抽出対象なので、述語に係る他の節を抽出する
        for src in dst_chunk.srcs:
            if src == chunk.id:
                continue
            
            src_chunk = chunks[src]
            src_particle = src_chunk.morph_of_pos('助詞', last=True)

            # 助詞を含まない場合は省略
            if src_particle is None:
                continue
            
            verb_phrase = chunk.phrase(True) + verb.base
            relations[verb_phrase].append((src_particle.base, src_chunk.phrase(True)))

    return relations

if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks

    chunks = get_neko_chunks(949)

    kakari = extract_sahen(chunks)

    for verb, values in sorted(kakari.items(), key=lambda item: item[0]):
        values = sorted(values, key=lambda v: v[0])
        o = verb
        o += '\t' + ' '.join(map(lambda v: v[0], values))
        o += '\t' + ' '.join(map(lambda v: v[1], values))
        print(o)