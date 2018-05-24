
if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks

    line8 = get_neko_chunks(8)

    for chunk in line8:
        o = chunk.sentence(True)
        if chunk.dst is not None:
            dst_chunk = line8[chunk.dst]
            o += '\t' + dst_chunk.sentence(True)
            print(o)