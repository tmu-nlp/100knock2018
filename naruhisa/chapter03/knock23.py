from knock20 import get_UK_data
import re

def get_section_list():
  return re.findall('==.*==', get_UK_data())


if __name__ == '__main__':
  pattern = re.compile('=+')
  for line in get_section_list():
    sec = pattern.match(line)
    print('セクションレベル:', len(sec.group()))
    print(re.sub('=', '', line))
