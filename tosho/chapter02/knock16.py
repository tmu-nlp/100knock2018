import argparse
import sys

# http://www.atmarkit.co.jp/ait/articles/1711/24/news016.html
# split -n file

# 余った部分は最後のファイルに書き出します。

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', type=int, default=10)
    parser.add_argument('file')

    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        blocks = arg.n
        lines = list(f)
        lines_per_block = int(len(lines) / blocks)
        for b_index in range(0, blocks):
            with open(f'out{b_index}.txt', 'w') as o:
                start_pos = b_index * lines_per_block
                end_pos = (b_index + 1) * lines_per_block
                # 最後のファイルにあまりを出力する
                if b_index == (blocks - 1):
                    end_pos = len(lines)
                o.writelines(lines[start_pos:end_pos])
