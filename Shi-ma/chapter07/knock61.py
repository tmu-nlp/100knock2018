import plyvel
import  argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('artist', type=str, help='artist')
    args = parser.parse_args()

    name_area_db = plyvel.DB('result/knock60_result.ldb', create_if_missing=False)
    name_artist = args.artist.encode('utf-8')
    if name_area_db.get(name_artist):
        print('{}: {}'.format(name_artist.decode('utf-8'), name_area_db.get(name_artist).decode('utf-8')))
    else:
        print('Not found.')
    name_area_db.close()
