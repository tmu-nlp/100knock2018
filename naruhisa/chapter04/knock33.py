from knock30 import *

if __name__ == '__main__':
  for sentence in ktskaiseki():
    for word in sentence:
      if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
        print(word['surface'])
