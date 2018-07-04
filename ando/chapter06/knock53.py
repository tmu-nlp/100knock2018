import sys
from pycorenlp import StanfordCoreNLP

def parse(path="/Users/one/klab/100knock2018/ando/chapter06/50out.txt"):
    nlp = StanfordCoreNLP("http://localhost:9000")
    prop = {"annotators":"tokenize, pos, lemma", "ner.useSUTime":False, "outputFormat":"xml"}
    text = open(path).read()
    tokenizedText = nlp.annotate(text, properties=prop).replace("<token ","\n<token ")
    return tokenizedText

if __name__ == "__main__":
    args = sys.argv[1] if len(sys.argv)>1 else "/Users/one/klab/100knock2018/ando/chapter06/50out.txt"
    print(parse(args))
