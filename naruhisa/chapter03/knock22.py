from knock20 import get_UK_data
import re 
import knock21


if __name__ == '__main__':
  for line in knock22.get_cate_list():
    line = re.sub('\[\[Category\:', '', line)
    line = re.sub('\]\]', '', line)
    print(line)

