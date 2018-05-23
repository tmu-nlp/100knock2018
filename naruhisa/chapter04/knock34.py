from knock30 import *

if __name__ == '__main__':
  for sentence in ktskaiseki():
    for i in range(len(sentence)):
      if sentence[i]['pos'] == '名詞':
        try:
          if sentence[i+2]['pos'] == '名詞' and sentence[i+1]['surface'] == 'の':
            print(sentence[i]['surface'], sentence[i+1]['surface'], sentence[i+2]['surface'])
        except:
          pass
      
