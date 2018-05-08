import gzip
import json


def search_country_data(country):
    for line in gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8'):
        json_data = json.loads(line)
        if json_data['title'] == country:
            return json_data['text']
    else:
        return None


def open_england():
    return open('england', encoding='utf-8')


if __name__ == '__main__':
    england = search_country_data('イギリス')
    with open('england', 'w', encoding='utf-8') as f:
        f.write(str(england))
    print(england)


# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．