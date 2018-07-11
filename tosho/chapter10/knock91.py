import sys

def main():
    section = sys.argv[1]
    
    current_section = None
    lines = 0
    for line in sys.stdin:
        line = line.strip()
        if line.startswith(': '):
            current_section = line[2:]
        elif current_section == section:
            print(line)
            lines += 1
        else:
            pass

    sys.stderr.write(f'{lines} lines saved.\n')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')