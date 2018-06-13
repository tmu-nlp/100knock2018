
if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks

    line8 = get_neko_chunks(8)

    for chunk in line8:
        if chunk.dst > -1:
            dst_chunk = line8[chunk.dst]
            if chunk.contains_pos('名詞') and dst_chunk.contains_pos('動詞'):
                o = f'{chunk.phrase(True)}\t{dst_chunk.phrase(True)}'
                print(o)