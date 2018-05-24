if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks
    from collections import defaultdict

    chunks = get_neko_chunks(8)

    kaku = defaultdict(set)
    for chunk in chunks:
        if chunk.dst is not None:
            dst_chunk = chunks[chunk.dst]
            if chunk.contains_pos('助詞') and dst_chunk.contains_pos('動詞'):
                kaku[dst_chunk.morph_of_pos('動詞').base].add(chunk.morph_of_pos('助詞').base)

    for verb, values in sorted(kaku.items(), key=lambda item: item[0]):
        values = sorted(values)
        o = verb + '\t' + ' '.join(values)
        print(o)