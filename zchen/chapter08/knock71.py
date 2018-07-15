from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from knock70 import make_data
from pickle import dump, load
from tqdm import tqdm
from re import compile
from iso639 import languages
from langdetect import detect, detect_langs
from os.path import isfile

re_w = compile(r'\w')

class Corpus:
    def __init__(self):
        if isfile('overview.pkl'):
            with open('overview.pkl', 'rb') as fr:
                self._languages = load(fr)
        else:
            self.from_data()
        self._second_fit()

    def from_data(self, data = make_data()):
        # overview of the data
        self._languages = {}
        for sent, tag in tqdm(data, desc = "Overview of data"):
            ch2 = detect(sent)
            lang = languages.get(alpha2 = ch2).name.lower()
            if lang not in self._languages:
                self._languages[lang] = [(sent, tag)]
            else:
                self._languages[lang].append((sent, tag))

        with open('overview.pkl', 'wb') as fw:
            dump(self._languages, fw)


    def _second_fit(self):
        remnants = self._languages.keys() - set(stopwords.fileids())
        rr = self._languages.keys() - set(SnowballStemmer.languages)
        print(remnants, rr - remnants)
        remnants |= rr
        for lang in remnants:
            print("Treating '%s' as english" % lang)
            for sent, tag in self._languages[lang]:
                print('  ', sent, '\t', detect_langs(sent))
            sents = self._languages.pop(lang)
            self._languages['english'] += sents


    def hand_engineering(self):
        _tok_tools = {}
        for lang in self._languages:
            _tok_tools[lang] = (set(stopwords.words(lang)), SnowballStemmer(lang))

        for lang, data in self._languages.items():
            for sent, tag in data:
                #sent = wordpunct_tokenize(sent)
                #sent = word_tokenize(sent, language = lang)
                sent = sent.strip().split()
                stopper, stemmer = _tok_tools[lang]
                sent = [stemmer.stem(w) for w in sent if w not in stopper and re_w.match(w)]
                if lang != 'english': # cuz it is a english task
                    stopper, stemmer = _tok_tools['english']
                    sent = [stemmer.stem(w) for w in sent if w not in stopper and re_w.match(w)]
                yield sent, tag
        #cnt = Counter() # tf-idf


if __name__ == '__main__':
    c = Corpus()
    #c.from_data()
    #print(tuple(c.hand_engineering()))
