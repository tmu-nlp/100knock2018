import json
import gzip
import plyvel



name_area_db = plyvel.DB('result/knock60_result.ldb', create_if_missing=True)  # データベースの作成 #
for line in gzip.open('../data/artist.json.gz'):
    data_dict = json.loads(line.decode('utf-8'))
    if set(['name', 'area']).issubset(set(data_dict.keys())):  # 内包されていれば #
        name_area_db.put(data_dict['name'].encode('utf-8'), data_dict['area'].encode('utf-8'))  # Levl DB は バイトでないと登録できない。(key, value) #
name_area_db.close()  # DBを閉じる必要がある。 #
