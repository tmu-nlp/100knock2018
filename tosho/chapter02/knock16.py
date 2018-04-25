import argparse

# split command
# http://www.atmarkit.co.jp/ait/articles/1711/24/news016.html
# - split command on macos does not have -n option...

# equivalent
# split -n 5 hightemp.txt

# usage
# python knock16.py -n 5 hightemp.txt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', type=int, default=10)
    parser.add_argument('file')

    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        blocks = arg.n
        lines = list(f)

        # 各ブロックに割り当てる行数を計算する
        # できるだけ均一に配分するようにする
        lines_in_blocks = [int(len(lines)/blocks) for i in range(blocks)]
        for i in range(len(lines) % blocks):
            lines_in_blocks[i] += 1
        # 累計を計算して、各ブロックの始点を特定する
        positions = [(sum(lines_in_blocks[:i])) for i in range(blocks)]

        for index, pos, amount in zip(range(blocks), positions, lines_in_blocks):
            with open(f'out{index}.txt', 'w') as o:
                o.writelines(lines[pos:(pos+amount)])
