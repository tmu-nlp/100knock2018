import knock41

def extractPath(chunk, sentence):
    path = [chunk]
    dst = chunk.dst
    while dst != -1:
        path.append(sentence[dst])
        dst = sentence[dst].dst
    return path

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = knock41.read_chunk(f)
    f.close()
    paths = []
    for sentence in sentences:
        for chunk in sentence:
            if chunk.include_pos('名詞') and chunk.dst != -1:
                paths.append(extractPath(chunk, sentence))

    for path in paths:
        print (" -> ".join([str(chunk) for chunk in path]))

#楽そのものすらも -> 感じ得ない
#日月を -> 切り落し -> 入る
#天地を -> 粉韲して -> 入る
#粉韲して -> 入る
#不可思議の -> 太平に -> 入る
#太平に -> 入る
#吾輩は -> 死ぬ
#太平を -> 得る
#太平は -> 得られぬ
