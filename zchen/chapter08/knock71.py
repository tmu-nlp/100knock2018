from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from knock70 import make_data
from iso639 import languages
from langdetect import detect, detect_langs
from collections import Counter
from pickle import dump, load
from tqdm import tqdm
from re import compile

_lang_stopwords_stemmers = {'english':(set(stopwords.words('english')), PorterStemmer())}
re_w = compile(r'\w')

def word_filter(sent_str):
    ch2 = detect(sent_str)
    lang = languages.get(alpha2 = ch2).name.lower()
    if lang not in _lang_stopwords_stemmers:
        #print(lang, sent_str)
        try:
            _lang_stopwords_stemmers[lang] = set(stopwords.words(lang)), SnowballStemmer(lang)
        except:
            lang = 'english'
    stopwords, stemmer = _lang_stopwords_stemmers[lang]

    sent_str = word_tokenize(sent_str, language = lang)
    cnt = Counter(stemmer.stem(w) for w in sent_str if w not in stopwords)
    return {k:v for k,v in cnt.items() if re_w.match(k)}, lang

def sent_filter(data):
    for sent, tag in tqdm(data):
        tokens, lang = word_filter(sent)
        yield tokens, lang, tag

def save_to(fname = 'data.pkl'):
    data = make_data()
    data = tuple(sent_filter(data))
    with open(fname, 'wb') as fw:
        dump(data, fw)

def check(fname = 'data.pkl'):
    from pprint import pprint
    with open(fname, 'rb') as fr:
        data = load(fr)
    print(len(data))
    lang_cnt = Counter(lang for toks, lang, tag in data)
    print(lang_cnt)
    #pprint(data)
    data = tuple((toks, tag) for toks, lang, tag in data)
    return zip(*data)

if __name__ == '__main__':
    check()
