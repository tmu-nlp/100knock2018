from collections import defaultdict
from sys import stdin, stderr

def main(country_code_file='countries'):    
    country_dict = defaultdict(dict)
    for line in open(country_code_file):
        line = line.strip()
        words = line.split()
        wl = len(words)
        if wl > 1:
            country_dict[wl][str(words)] = '_'.join(words)

    frames = list(country_dict.keys())
    
    for i, line in enumerate(stdin):
        if i % 10000 == 0:
            stderr.write(f'{i} lines loaded\n')
        
        line = line.rstrip()
        words = line.split()
        
        ret = []
        for i, word in enumerate(words):
            ret.append(word)
            for frame in frames:
                if len(ret) > frame:
                    sub_words = ret[-frame]
                    if str(sub_words) in country_dict[frame]:
                        ret = ret[:-frame]
                        ret.append('_'.join(sub_words))

        print(' '.join(ret))

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')