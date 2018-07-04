import xml.etree.ElementTree as ET
import collections



def make_sentences_list(data_in_path):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    sentence_list = [None]

    for sentence in root.findall(".//sentences/sentence"):
        temp = [None]
        for word in sentence.findall(".//word"):
            temp.append(word.text)
        sentence_list.append(temp)
    return sentence_list


def make_coref_dict(data_in_path, sentence_list):
    coref_dict = collections.defaultdict(list)
    tree = ET.parse(data_in_path)
    root = tree.getroot()

    for coreference in root.findall(".//coreference/coreference"):
        for mention in coreference.findall(".//mention"):
            sentence_id = int(mention.find('sentence').text)
            start_id = int(mention.find('start').text)
            end_id = int(mention.find('end').text)

            if mention.get('representative') == 'true':
                representative_text = ' '.join(sentence_list[sentence_id][start_id:end_id])
            elif mention.get('representative') == None:
                coref_dict[sentence_id].append((start_id, end_id, representative_text))
    return coref_dict


def replace_mention(data_in_path, data_out):
    sentence_list = make_sentences_list(data_in_path)
    coref_dict = make_coref_dict(data_in_path, sentence_list)

    for sentence_id in range(1, len(sentence_list)):
        word_list = sentence_list[sentence_id]
        flag_list = [1 for i in range(len(word_list))]
        temp = dict()

        if sentence_id in coref_dict.keys():
            for start_id, end_id, rep in sorted(coref_dict[sentence_id], key=lambda x: x[1] - x[0], reverse=True):
                if 0 in flag_list[start_id:end_id]:
                    continue
                else:
                    temp[start_id] = '「{}（{}）」'.format(rep, ' '.join(word_list[start_id:end_id]))
                    flag_list[start_id:end_id] = [0 for i in range(end_id - start_id)]
            for flag_id in range(1, len(flag_list)):
                if flag_list[flag_id] != 0:
                    temp[flag_id] = word_list[flag_id]
                else:
                    continue
            yield ' '.join([temp[key] for key in sorted(temp.keys())])
        else:
            yield ' '.join(word_list[1:])



if __name__ == '__main__':
    with open('./result/knock56.txt', 'w') as data_out:
        data_in_path = '../data/knock50.txt.xml'
        for line in replace_mention(data_in_path, data_out):
            print(line, file=data_out)



# filter 関数 で filter(lambda: 式)の式がfalseなら飛ばされる
