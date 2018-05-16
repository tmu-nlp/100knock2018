from knock20 import get_UK_data
import re

def get_file_list():
  return re.findall('\[\[ファイル:.*\]\]', get_UK_data())

if __name__ == '__main__':
  for line in get_file_list():
    line = re.sub('\[\[ファイル:', '', line)
    line = re.sub('\|.*', '', line)
    print(line)
