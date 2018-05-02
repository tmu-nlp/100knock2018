# -*- coding: utf-8 -*-
import sys

def split_1(f, n):
    line = [line.strip() for line in f]
    ans = []
    if n > len(line):
        return '分割できません'
    else:
        for i in range(n):
            ans.append(line[i::n])
        return ans

def split_2(f, n):
    line = [line.strip() for line in f]
    N = int(len(line) / n)
    s = 0
    ans = []
    if n > len(line):
        return '分割できません'
    else:
        for i in range(n):
            ans.append(line[s:s+N])
            s += N
        return ans


if __name__ == '__main__':
    file = open('hightemp.txt', 'r')
    n = int(sys.argv[1])

    print(split_1(file, n))
    print(split_2(file, n))

