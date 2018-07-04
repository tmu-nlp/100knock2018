from knock71 import StopWords
from stemming.porter2 import stem
from collections import defaultdict
import numpy as np
import pickle as pkl

def main():
    stop_word = StopWords()
    feat_map = FeatureMap(stop_words=stop_word)
    
    for line in open('sentiment.txt'):
        feat_map.learn_feats(line)
    
    print(f'{len(feat_map.id_dict)} features learned.')
    save_feat_map(feat_map)

def save_feat_map(feat_map, file_name='feat_map.pkl'):
    with open(file_name, 'wb') as f:
        pkl.dump(dict(feat_map.id_dict), f)

def load_feat_map(file_name='feat_map.pkl'):
    with open(file_name, 'rb') as f:
        id_dict = pkl.load(f)
        return FeatureMap(id_dict=id_dict)

class FeatureMap:
    def __init__(self, id_dict={}, stop_words=StopWords()):
        if len(id_dict) == 0:
            self.id_dict = defaultdict(lambda:len(self.id_dict))
            self.id_dict['UNK'] = 0
        else:
            self.id_dict = id_dict
        self.stop_words = stop_words
        self.rev_id_dict = None

    def extract_feat_tokens(self, line):
        tokens = []
        for w in line.rstrip().split():
            w = stem(w.lower())
            if self.stop_words.is_stop_word(w) == False:
                tokens.append(w)
        return tokens

    def learn_feats(self, line):
        for t in self.extract_feat_tokens(line):
            self.id_dict[t]

    def extract_feats(self, line):
        feats = []
        for t in self.extract_feat_tokens(line):
            if t in self.id_dict:
                feats.append(self.id_dict[t])
            else:
                # unk
                feats.append(0)
        return np.array(feats)
    
    def extract_one_hot(self, line):
        one_hot = np.zeros(len(self.id_dict))
        for f in self.extract_feats(line):
            one_hot[f] += 1
        return one_hot
    
    def get_feat_token(self, feat_id):
        if self.rev_id_dict == None:
            self.rev_id_dict = dict()
            for k, v in self.id_dict.items():
                self.rev_id_dict[v] = k
        if feat_id in self.rev_id_dict:
            return self.rev_id_dict[feat_id]
        else:
            return None

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')