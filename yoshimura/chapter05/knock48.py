from knock41 import get_chunk_list

with open('result48','w') as output_file:
    for line in get_chunk_list():
        for chunk in line:
            if chunk.check_pos('名詞'):
                output_file.write(chunk.normalized_surface())

                dst = chunk.dst
                while dst != -1:
                    output_file.write(f'-> {line[dst].normalized_surface()}')
                    dst = line[dst].dst
                output_file.write('\n')





            