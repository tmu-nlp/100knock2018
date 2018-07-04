from sys import stdin

def main():
    for i, line in enumerate(stdin):
        line = line.rstrip()
        words = line.split()
        ret = []
        for w in words:
            w = w.strip('.,!?;:()[]''"')
            if len(w) > 0:
                ret.append(w)
        if len(ret) > 0:
            print(' '.join(ret))

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')