from knock26 import *
import re

if __name__ == '__main__':
  base_info = load_bain('base_info2.pkl')
  for k, v in base_info.items():
    base_info[k] = re.sub('\<.*\>', '', v)
  print(base_info)
  save_bain(base_info, 'base_info3.pkl')
