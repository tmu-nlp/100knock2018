import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    lines = 0
    with open(arg.file, 'r') as f:
        for l in f:
            lines += 1
    
    print(lines)
