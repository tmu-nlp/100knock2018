import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        temps = list(map(lambda line: float(line.split('\t')[2]), f))

    sorted(temps)

    for t in temps:
        print(t)