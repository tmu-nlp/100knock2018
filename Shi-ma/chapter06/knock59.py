import xml.etree.ElementTree as ET



def make_NP_split_list(s_list):
    if '(NP' not in s_list:
        return
    else:
        count = 0
        NP_split = list()
        for s in s_list:
            if count == 0:
                if s == '(NP':
                    count += 1
                    NP_split.append(s)
            else:
                if '(' in s:
                    count += 1
                    NP_split.append(s)
                elif ')' in s:
                    count -= s.count(')')
                    NP_split.append(s)
                if count <= 0:
                    yield from make_NP_split_list(NP_split[1:])
                    yield NP_split
                    count = 0
                    NP_split = list()


def S2text(NP_split):
    temp = list()
    for p in NP_split:
        if ')' in p:
            temp.append(p.replace(')', ''))
        else:
            continue
    return ' '.join(temp)


def find_NP(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()

    for sentence in root.findall(".//sentences/sentence"):
        s_list = sentence.find('parse').text.split()
        for NP_split in make_NP_split_list(s_list):
            yield S2text(NP_split)
        yield ''


if __name__ == '__main__':
    with open('./result/knock59.txt', 'w') as data_out:
        data_in_path = '../data/knock50.txt.xml'
        for line in find_NP(data_in_path, data_out):
            print(line, file=data_out)
