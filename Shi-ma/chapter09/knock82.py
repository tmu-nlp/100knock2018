import random



if __name__ == '__main__':
    with open('result/knock82_result.txt', 'w') as data_out:
        for line in open('result/knock81_result.txt', 'r'):
            tokens = line.split()
            for i in range(len(tokens)):
                d = random.randint(1, 5)
                for j in range(-d, d+1):
                    c = ''
                    if j == 0:
                        t = tokens[i]
                    elif i + j < 0:
                        continue
                    elif i + j > len(tokens) - 1:
                        continue
                    else:
                        c = tokens[i + j]

                    if c == '':
                        continue
                    else:
                        print('\t'.join([t, c]), file=data_out)

