from knock26 import *

if __name__ == '__main__':
  base_info = load_bain('base_info3.pkl')

  for k, v in base_info.items():
    v = re.sub('\[\[.*\|', '', v)
    v = re.sub('\]\]', '', v)
    v = re.sub('\{\{.*\|', '',  v)
    v = re.sub('\}\}', '', v)
    base_info[k] = re.sub('\[\[', '', v)
  print(base_info)
