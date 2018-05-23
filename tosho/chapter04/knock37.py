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

    words = sorted(words.items(), key=lambda item: item[1], reverse=True)

    words = words[:10]

    occurences = list(map(lambda item: item[1], words))
    words = list(map(lambda item: item[0], words))

    # 頻度はすでにカウントしてあるので、barで描写する
    # histは、系列内を自動で集計するため、今回の状況では利用しない
    plt.bar(words, occurences)
    plt.title('頻度上位10語')
    plt.show()

'''
参考：matplotlibで日本語が文字化けする
http://kaisk.hatenadiary.com/entry/2015/02/15/215831
'''