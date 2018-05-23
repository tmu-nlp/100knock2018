import pickle
import re

def load_bain(file_name):
  with open(file_name, 'rb') as f:
    return pickle.load(f)

def save_bain(obj, file_name):
  with open(file_name, 'wb') as f:
    pickle.dump(obj, f)


if __name__ == '__main__':
  base_info = load_bain('base_info.pkl')
  for k, v in base_info.items():
    base_info[k] = re.sub('\'{3}|\'{5}|\'{2}', '', v)
  print(base_info)
  save_bain(base_info, 'base_info2.pkl')
