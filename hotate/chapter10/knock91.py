# -*- coding: utf-8 -*-


def main():
    with open('knock91.txt', 'w') as f:
        for line in open('questions-words.txt', 'r'):
            l = line.strip().split()
            if l[0] == ':':
                section = l[1]
            elif section == 'family':
                print(line.strip(), file=f)


if __name__ == '__main__':
    main()
