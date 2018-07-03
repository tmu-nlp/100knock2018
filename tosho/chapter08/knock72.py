from knock71 import StopWords
from stemming.porter2 import stem

def main():
    test_sent = '+1 I have a pen .'
    feats = extract_feat(test_sent)

    print(feats)

def extract_feat(line, stop_words=StopWords()):
    feat = {}
    for w in line.rstrip().split():
        if w == '-1' or w == '+1':
            continue
        w = w.lower()
        w = stem(w)
        if stop_words.is_stop_word(w) == False:
            feat[w] = 1
    return feat

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')