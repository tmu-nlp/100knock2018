import gzip
import json

def get_UK_data():
  with gzip.open('jawiki-country.json.gz', 'r', 'utf-8') as f:
    for line in f:
      obj = json.loads(line.decode('utf-8'))
      if obj['title'] == 'イギリス':
        return obj['text']
if __name__ == '__main__':
  print(get_UK_data())
