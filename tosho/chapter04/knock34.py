if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter04.knock30 import iterate_neko
    from collections import defaultdict

    phrases = defaultdict(int)

    for morphs in iterate_neko():
        for m1, m2, m3 in zip(*[morphs[i:] for i in range(3)]):
            if m1.pos == '名詞' and \
                m2.surface == 'の' and \
                m3.pos == '名詞':
                phrase = m1.surface + m2.surface + m3.surface
                phrases[phrase] += 1

    for v, c in phrases.items():
        print(f'{v} ({c} times)')

    print('----------')
    print(f'{len(phrases)} phrases')