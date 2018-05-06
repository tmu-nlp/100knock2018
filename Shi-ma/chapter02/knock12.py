# cat ../data/hightemp.txt | cut -f1 # # col1.txt
# cat ../data/hightemp.txt | cut -f2 # # col2.txt

def split_line(separator, path):
    for line in open(path):
        yield line.strip().split(separator)



if __name__ == '__main__':
    path = '../data/hightemp.txt'

    with open('../data/col1.txt', 'w') as col1_out, open('../data/col2.txt', 'w') as col2_out:
        for col_list in split_line('\t', path):
            col1_out.write(col_list[0] + '\n')
            col2_out.write(col_list[1] + '\n')
