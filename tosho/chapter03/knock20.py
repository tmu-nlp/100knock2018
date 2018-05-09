import json

def query_article(path='./jawiki-country.json', query='イギリス'):
    with open(path, 'r', encoding='utf-8') as src:
        data = [json.loads(line) for line in src]
        for item in data:
            if query in item['title']:
                yield item

if __name__ == '__main__':
    results = query_article()
    for i, article in enumerate(results):
        for line in article['text'].split('\n'):
            print(line)
