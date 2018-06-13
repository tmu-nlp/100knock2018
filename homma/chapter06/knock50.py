import re

def get_nlp_iter(n=-1):
    cnt = 0
    for line in open('nlp.txt', encoding='utf8'):
        line = line.rstrip()
        if not line:
            continue
        ptn = re.compile(r'(?<=[.;:?!])\s(?=[A-Z])')
        sentences = re.split(ptn, line)

        for sentence in sentences:
            if cnt == n:
                return
            yield sentence
            cnt += 1

if __name__ == '__main__':
    with open('nlp_lines.txt', 'w', encoding='utf8') as f:
        for line in get_nlp_iter():
            f.write(line + '\n')


''' 問
50. 文区切り

(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．
'''

''' 実行結果
Natural language processing
From Wikipedia, the free encyclopedia
Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
As such, NLP is related to the area of humani-computer interaction.
Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
History
The history of NLP generally starts in the 1950s, although work can be found from earlier periods.
In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence.
The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English.
The authors claimed that within three or five years, machine translation would be a solved problem.
'''
