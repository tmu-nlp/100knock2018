#素性抽出
import codecs 
import snowballstemmer #提取词干
from collections import Counter
from knock71 import StopWord
fencoding = 'latin-1'

f_sentiment = 'sentiment.txt'
f_features = 'features.txt'

stemmer = snowballstemmer.stemmer('english')
word_counter = Counter()

with codecs.open(f_sentiment,'r',encoding='latin-1')as f_in:
    for line in f_in:
        for word in line[2:].split(' '):
            word = word.strip()
            a = StopWord(list)
            if a.exists(str):
                continue
            word = stemmer.stemWord(word)

            if word != '!' and word !='?' and len(word)<=1:
                continue

            word_counter.update([word])

features = [word for word, count in word_counter.items() if count >=6]

with codecs.open(f_features,'w',encoding='latin-1')as f_out:
    print(*features,sep='\n',file=f_out)

