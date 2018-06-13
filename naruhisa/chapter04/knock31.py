from knock30 import *

if __name__ == '__main__':
  for sentence in ktskaiseki():
    for word in sentence:
      if word['pos'] == '動詞':
        print(word['surface'])
