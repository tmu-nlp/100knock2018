if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter04.knock30 import iterate_neko
    from collections import defaultdict
    import matplotlib.pyplot as plt

    words = defaultdict(int)

    for morphs in iterate_neko():
        for m in morphs:
            words[m.base] += 1

    freq = sorted(words.values(), reverse=True)
    rank = list(range(1, len(freq)+1))
    
    plt.plot(rank, freq)
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel('rank')
    plt.ylabel('frequency')

    plt.title("Zipf's law")
    plt.show()
