if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter04.knock30 import iterate_neko
    from collections import defaultdict

    phrases = defaultdict(int)

    for morphs in iterate_neko():
        nouns = []

        morphs.append(None) # 後門番
        for m in morphs:
            if m == None or m.pos != '名詞':
                if len(nouns) > 0:
                    p = ''.join(map(lambda a: a.surface, nouns))
                    phrases[p] += 1
                    nouns = []
            else:
                nouns.append(m)
        
    for v, c in phrases.items():
        print(f'{v} ({c} times)')

    print('----------')
    print(f'{len(phrases)} phrases')