from knock41 import get_chunk_list

for line in get_chunk_list():
    for chunk in line:
        if chunk.check_pos('動詞'):
            predicate = chunk.get_surfaces('pos', '動詞')[0]
            
            avs = []
            for src in chunk.srcs:
                if len(line[src].get_surfaces('pos', '助詞')) > 0:
                    avs.append(line[src].get_surfaces('pos', '助詞').pop())
            
            if avs:
                avs = ' '.join(sorted(avs))
                print(f'{predicate}\t{avs}')
        

# sort result45 | uniq -c | sort -n -r  > result45_unix
# grep "^する" result45 | sort | uniq -c | sort -n -r > する
# grep "^見る" result45 | sort | uniq -c | sort -n -r > 見る
# grep "^与える" result45 | sort | uniq -c | sort -n -r > 与える
