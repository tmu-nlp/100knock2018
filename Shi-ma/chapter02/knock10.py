# wc -l '../data/hightemp.txt'

def count_line(path):
    return sum([1 for line in open(path)])

if __name__ == '__main__':
    path = '../data/hightemp.txt'

    print(count_line(path))
