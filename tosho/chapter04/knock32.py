if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter04.knock30 import iterate_neko
    from collections import defaultdict

    verbs = defaultdict(int)

    for morphs in iterate_neko():
        for m in morphs:
            if m.pos == '動詞':
                verbs[m.base] += 1

    for v, c in verbs.items():
        print(f'{v} ({c} times)')

    print('----------')
    print(f'{len(verbs)} verbs(base)')