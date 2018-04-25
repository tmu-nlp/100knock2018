import argparse

newline = '\n'
tab = '\t'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input1')
    parser.add_argument('input2')
    parser.add_argument('out')
    arg = parser.parse_args()

    with open(arg.input1, 'r') as i1:
        with open(arg.input2, 'r') as i2:
            lines = zip(
                i1.read().splitlines(),
                i2.read().splitlines()
            )

            with open(arg.out, 'w') as o:
                for line in lines:
                    o.write(line[0] + tab + line[1] + newline)
