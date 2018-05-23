if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter04.knock30 import iterate_neko
    from collections import defaultdict

    words = defaultdict(int)

    for morphs in iterate_neko():
        for m in morphs:
            words[m.base] += 1

    words = sorted(words.items(), key=lambda item: item[1], reverse=True)

    for v, c in words[:100]:
        print(f'{v} ({c} times)')

    print('...')
    print('----------')
    print(f'{len(words)} words')