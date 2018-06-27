import json
import gzip
import plyvel
import pickle
import argparse



def make_name_tags_DB(data_js_path):
    name_tags_db = plyvel.DB('result/knock63_result.ldb', create_if_missing=True)
    for line in gzip.open(data_js_path):
        data_dict = json.loads(line.decode('utf-8'))
        if set(['name', 'tags']).issubset(set(data_dict.keys())):
            name_tags_db.put(data_dict['name'].encode('utf-8'), pickle.dumps(data_dict['tags']))
    name_tags_db.close()


def load_make_tags_DB(data_ldb_path, data_out_path):
    with open(data_out_path, 'w') as data_out:
        name_tags_db = plyvel.DB(data_ldb_path, create_if_missing=True)
        for key, tags_serialized in name_tags_db:
            tags_dict = pickle.loads(tags_serialized)[0]
            print('name: {}\ttag: {}\ttag_count: {}'.format(key.decode('utf-8'), tags_dict['value'], tags_dict['count']), file=data_out)
        name_tags_db.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='make or load')
    args = parser.parse_args()

    data_js_path = '../data/artist.json.gz'
    data_ldb_path = 'result/knock63_result.ldb'
    data_out_path = 'result/knock63_result.txt'

    if args.mode == 'make':
        make_name_tags_DB(data_js_path)
    elif args.mode == 'load':
        load_make_tags_DB(data_ldb_path, data_out_path)
