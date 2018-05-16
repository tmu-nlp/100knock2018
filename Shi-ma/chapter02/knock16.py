# split -l N ../data/hightemp.txt split.txt

import argparse
import glob
import os



def txt_file_split(path, N):
    split_file = list()
    for line in open(path):
        split_file.append(line.strip())
        if len(split_file) == N:
            yield split_file
            split_file = list()
    if len(split_file) != 0:
        yield split_file



# listを用いる場合
# def txt_file_split(path, N):
#     line_list = [line.strip() for line in open(path)]
#
#     for i in range(0, len(line_list), N):
#         yield line_list[i:i+N]



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', type=int, default=1, help='N lines split')
    parser.add_argument('-O', type=str, default='../data/hightemp_split', help='Output directory')
    parser.add_argument('path')

    args = parser.parse_args()

    path_list = glob.glob('{}/split*.txt'.format(args.O))
    for path in path_list:
        os.remove(path)

    for i, split_file in enumerate(txt_file_split(args.path, args.N)):
        with open('{}/split{}.txt'.format(args.O, i+1), 'w') as output_file:
            for line in split_file:
                output_file.write(line + '\n')
