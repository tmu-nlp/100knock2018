# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def check_num(mentions, men_num, add):
    next_num = men_num + 1 + add
    if next_num < len(mentions):
        if mentions[next_num][1] <= mentions[men_num][2] and mentions[next_num][0] == mentions[men_num][0]:
            add += 1
            return check_num(mentions, men_num, add)
    return add


if __name__ == '__main__':
    tree = ET.parse('knock50.txt.xml')

    sentences = []
    for sentence in tree.iter('sentence'):
        word_list = []
        for word in sentence.iter('word'):
            word_list.append(word.text)
        if len(word_list) > 0:
            sentences.append(word_list)

    mentions = []
    m = []
    for mention in tree.iter('mention'):
        if mention.attrib:
            representative = mention.find('text').text
        else:
            mentions.append([
                int(mention.find('sentence').text) - 1,
                int(mention.find('start').text) - 1,
                int(mention.find('end').text) - 2,
                mention.find('text').text,
                representative
            ])

    mentions = sorted(mentions, key=lambda x: x[1])
    mentions = sorted(mentions, key=lambda x: x[0])

    with open('knock56.txt', 'w') as f:
        men_num = 0
        for sent_num, sentence in enumerate(sentences):
            word_num = 0
            for j in range(len(sentence)):
                if word_num == len(sentence):
                    break
                if men_num < len(mentions):
                    if mentions[men_num][0] == sent_num and mentions[men_num][1] == word_num:
                        f.write(f'{mentions[men_num][4]} ({mentions[men_num][3]}) ')
                        word_num = mentions[men_num][2]
                        add_num = check_num(mentions, men_num, add=0)
                        men_num += 1 + add_num
                        continue
                word = sentence[word_num]
                f.write(f'{word} ')
                word_num += 1
            print(file=f)
