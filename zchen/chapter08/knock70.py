import tarfile
from random import shuffle

def _load_data():
    data = {'pos': [], 'neg': []}
    with tarfile.open("rt-polaritydata.tar.gz", 'r:gz') as tarf:
        for tag, content in data.items():
            for member in tarf.getmembers():
                if member.name.endswith(tag):
                    with tarf.extractfile(member.name) as fr:
                        for line in fr:
                            content.append(line.decode('latin-1').strip())
    return data

def make_data():
    data = _load_data()
    pos = [(s,+1) for s in data['pos']]
    neg = [(s,-1) for s in data['neg']]
    data = pos + neg
    shuffle(data)
    return data


m = make_data()
