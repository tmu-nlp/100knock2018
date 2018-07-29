def load_analogy(fname = 'questions-words.txt', ncols = 4):
    data = {}
    key = None
    with open(fname) as fr:
        for line in fr:
            if line.startswith(': '):
                key = line[2:-1]
                data[key] = []
            else:
                toks = line[:-1].split()
                if len(toks) == ncols:
                    data[key].append(toks)
                else:
                    raise ValueError(line[:-1])
    return data

def write_analogy(fname, data):
    with open(fname, 'w') as fw:
        for key, analogies in data.items():
            fw.write(': %s\n' % key)
            for analogy in analogies:
                fw.write(' '.join(analogy) + '\n')

if __name__ == "__main__":
    fa = load_analogy()['family']
    write_analogy('knock91.txt', {'family':fa})
