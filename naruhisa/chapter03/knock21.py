from knock20 import get_UK_data
import re

def get_cate_list():
  return re.findall('\[\[Category:.*\]\]', get_UK_data())

if __name__ == '__main__':
  print(get_cate_list())
