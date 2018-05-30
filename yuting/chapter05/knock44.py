#44. 係り受け木の可視化

import knock41
import knock42
import pydot

def sentenceToDot(idx, sentence):
    head = "digraph sentence{0} ".format(idx)
    body_head = "{ graph [rankdir = LR]; "
    body = ""
    for chunk_pair in sentence:
        former, latter = chunk_pair
        body += ('"'+str(former)+'"->"'+str(latter)+'"; ')
    dotString = head + body_head + body + '}'
    return dotString


if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = knock41.read_chunk(f)
    pair_sentences = []
    for sentence in sentences:
        pair = knock42.make_chunk_pair(sentence)
        pair_sentences.append(pair)
    dotStrings = []
    for idx, sentence in enumerate(pair_sentences):
        dotString = sentenceToDot(idx, sentence)
        print (dotString)
        dotStrings.append(dotString)
    f.close()