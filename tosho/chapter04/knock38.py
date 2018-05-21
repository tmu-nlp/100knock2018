if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter04.knock30 import iterate_neko
    from collections import defaultdict
    import matplotlib.pyplot as plt

    words = defaultdict(int)

    for morphs in iterate_neko():
        nouns = []

        for m in morphs:
            words[m.base] += 1

    occurences = words.values()

    plt.hist(occurences, bins=100, log=True)
    plt.title(f'出現頻度ごとの単語誤り数(最大頻度:{max(occurences)})')
    plt.show()
