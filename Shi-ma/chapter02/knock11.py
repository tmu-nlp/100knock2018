# cat ../data/hightemp.txt | tr '\t' ' '

def tab_to_space(path):
    for line in open(path):
        yield line.replace('\t', ' ').strip()



if __name__ == '__main__':
    path = '../data/hightemp.txt'

    for line in tab_to_space(path):
        print(line)
