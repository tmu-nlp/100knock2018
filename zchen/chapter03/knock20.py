from collections import Counter
import gzip
import json


def get_data(fname = "jawiki-country.json.gz"):
    with gzip.open(fname) as fr:
        for line in fr:
            line = json.loads(line)
            yield line["title"], line["text"]

def filter_english():
    for title, text in get_data():
        if title == "イギリス":
            return text.split('\n')

if __name__ == "__main__":
    c = Counter(title for title, _ in get_data())
    c = filter(lambda x:x[1] > 1, c.items())
    for i in c:
        print("%s:%d" % i)
        exit()
    else:
        print("Examined: every title is unique")
        for line in filter_english():
            print(line)
