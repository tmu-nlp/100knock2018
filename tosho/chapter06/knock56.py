# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from chapter06.knock53 import load_nlp_sentences
from common.parsers import load_corenlp_coreference
from collections import defaultdict

def load_nlp_coref(file_name='./nlp.txt.xml'):
    return load_corenlp_coreference(file_name)

def tokens_to_str(tokens):
    return ' '.join(map(lambda t: t.word, filter(lambda t2: t2.word is not None, tokens)))

if __name__ == '__main__':
    tokens = list(load_nlp_sentences())
    sentences = defaultdict(list)
    for t in tokens:
        sentences[t.sentence_id].append(t)
    
    # 参照元のwordフィールドを置き換えることで、表示を変更する
    for coref in load_nlp_coref():
        repr = coref.representative

        print(f'{repr.sentence_id}({repr.start}..{repr.end}) -> {len(coref.mentions)-1}')
        repr_tokens = sentences[repr.sentence_id][repr.start-1:repr.end-1]
        repr_text = tokens_to_str(repr_tokens)

        for m in coref.mentions:
            if m == repr:
                continue
            else:
                sentence = sentences[m.sentence_id]

                tokens = sentence[m.start-1:m.end-1]
                ref_text = tokens_to_str(tokens)

                tokens[0].word = f'{repr_text} ({ref_text})'
                for t in tokens[1:]:
                    t.word = None
    
    for i, token in sentences.items():
        print(tokens_to_str(token))
