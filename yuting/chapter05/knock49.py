from collections import namedtuple
from itertools import combinations
import knock41

def extractPathIndex(i_chunk, sentence):
    i, chunk = i_chunk
    path_index = [i]
    dst = chunk.dst
    while dst != -1:
        path_index.append(dst)
        dst = sentence[dst].dst
    return path_index

def posReplace(chunks, pos, repl, k=1):
    replaced_str = ""
    for morph in chunks[0].morphs:
        if morph.pos == pos and k > 0:
            replaced_str += repl
            k -= 1
        else:
            if morph.pos != '記号':
                replaced_str += morph.surface
    return [replaced_str] + [str(chunk) for chunk in chunks[1:]]


if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = knock41.read_chunk(f)
    f.close()
    paths = []
    N2Npath = namedtuple('N2Npath', ['X', 'Y', 'is_linear'])
    for sentence in sentences:
        noun_chunks = [(i, chunk) for i, chunk in enumerate(sentence) if chunk.include_pos('名詞')]
        if len(noun_chunks) > 1:
            for former, latter in combinations(noun_chunks, 2):
                f_index = extractPathIndex(former, sentence)
                l_index = extractPathIndex(latter, sentence)
                f_i, l_i = list(zip(reversed(f_index), reversed(l_index)))[-1]
                linear_flag = (f_i == l_i)
                if linear_flag:
                    f_index2 = f_index[:f_index.index(f_i)+1]
                    l_index2 = l_index[:l_index.index(l_i)+1]
                else:
                    f_index2 = f_index[:f_index.index(f_i)+2]
                    l_index2 = l_index[:l_index.index(l_i)+2]
                X = [sentence[k] for k in f_index2]
                Y = [sentence[k] for k in l_index2]
                paths.append(N2Npath(X=X, Y=Y, is_linear=linear_flag))

    for path in paths:
        x = posReplace(path.X, "名詞", "X")
        y = posReplace(path.Y, "名詞", "Y")
        if path.is_linear:
            x[-1] = "Y"
            print (" -> ".join(x))
        else:
            print ("%s | %s | %s" % (" -> ".join(x[:-1]), " -> ".join(y[:-1]), path.X[-1]))

#に -> いても | Yは | ない
#Xを | Yを | 切り落し
#Xを -> 切り落し | Y韲して | 入る
#Xを | Yの | 切り落し
#Xを -> 切り落し | Yに | 入る
#Xを -> Y
#Xを | Yの | 粉韲して
#Xを -> 粉韲して | Yに | 入る
#X韲して | Yの -> 太平に | 入る
#X韲して | Yに | 入る