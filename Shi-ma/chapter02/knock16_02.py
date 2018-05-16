# split -l N ../data/hightemp.txt split.txt
# ファイルをN分割

import argparse
import glob
import os



def txt_file_split(path, N):
    length = sum([1 for line in open(path)])
    split_file = list()

    if N > length:
        print('分割数が多すぎます。もう一度実行してください。')
        exit()
    else:
        count = 0
        for i, line in enumerate(open(path)):
            split_file.append(line.strip())
            if (i + 1) % int(length / N) == 0 and count != (N - 1):
                count += 1
                yield split_file
                split_file = list()
        if len(split_file) != 0:
            yield split_file


# listを用いる場合
# def txt_file_split(path, N):
    # line_list = [line.strip() for line in open(path)]
    #
    # split_len = int(len(line_list)/N)
    # if N > len(line_list):
    #     print('分割数が多すぎます。もう一度実行してください。')
    #     exit()
    # else:
    #     for count, i in enumerate(range(0, len(line_list), split_len)):
    #         if (count + 1) < N:
    #             yield line_list[i:i+split_len]
    #         else:
    #             yield line_list[i:]
    #             break



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
