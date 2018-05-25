if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks

    chunks = get_neko_chunks(8)

    for chunk in chunks:
        if chunk.morph('名詞') is not None:
            o = chunk.phrase(True)

            dst = chunk.dst
            while dst is not None:
                dst_chunk = chunks[dst]
                o += ' -> ' + dst_chunk.phrase(True)
                dst = dst_chunk.dst
            
            print(o)
