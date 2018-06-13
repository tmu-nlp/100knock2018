import sys
import re

p = re.compile('.*[.;:?!][\s\\n]+(?=[A-Z])')

def sentence(path="/Users/one/Downloads/nlp.txt"):
    sentences = re.findall(p,open(path).read())
    return sentences

if __name__ == "__main__":
    args = sys.argv[1] if len(sys.argv)>1 else "/Users/one/Downloads/nlp.txt" 
    with open("50out.txt","w")as f:
        for i in sentence(args):
            i = i.strip() + "\n"
            f.write(i)
