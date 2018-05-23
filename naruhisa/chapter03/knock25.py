from knock20 import get_UK_data
import re
import pickle

if __name__ == '__main__':
  flag = 0
  base_info = dict()
  for line in get_UK_data().split('\n'):
    if '基礎情報' in line:
      flag = 1
      #print(line, '\n')
    elif flag == 1 and line == '}}':
      flag = 0
      #print(line)
    elif flag == 1:
      line = line.split(' = ')
      try:
        base_info[line[0][1:]] = line[1]
      except:
        pass
  print(base_info)
  with open('base_info.pkl', 'wb') as f:
    pickle.dump(base_info, f)
      
