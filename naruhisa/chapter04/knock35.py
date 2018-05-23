from knock30 import *

if __name__ == '__main__':
  for sentence in ktskaiseki():
    flag = False
    tmp = list()
    for word in sentence:
      if word['pos'] == '名詞':
        flag = True
      if flag and word['pos'] != '名詞':
        print(''.join(tmp))
        tmp = list()
        flag = False
      elif flag:
        tmp.append(word['surface'])
