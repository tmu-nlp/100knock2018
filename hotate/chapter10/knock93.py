# -*- coding: utf-8 -*-


def compare(path):
    corr = 0
    for count, line in enumerate(open(path, 'r')):
        line = line.strip().split()
        if line[3] == line[4]:
            corr += 1

    accuracy = corr / (count+1)
    return accuracy


if __name__ == '__main__':
    accuracy = compare('knock92_90.txt')
    print(f'90 accuracy = {accuracy}')
    accuracy = compare('knock92_85.txt')
    print(f'85 accuracy = {accuracy}')

