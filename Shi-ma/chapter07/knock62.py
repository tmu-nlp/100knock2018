import plyvel

name_area_db = plyvel.DB('result/knock60_result.ldb', create_if_missing=False)
count_jap = sum([1 for key, value in name_area_db if value.decode('utf-8') == 'Japan'])
print(count_jap)
name_area_db.close()
