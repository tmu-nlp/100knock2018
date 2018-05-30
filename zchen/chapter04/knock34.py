from knock30 import *

def extract_no_phase():
    ret = set()
    for line in line_gen():
        result = re_fields.match(line)
        last_result = None
        weaving = False
        if result:
            if weaving and result.group('品詞') == '名詞':
                if isinstance(tuple, last_result):
                    last_result = (last_result, result)
                last_result = result
                weaving = False
            elif last_result and result.group('品詞細分類1') == '連体化':
                last_result = (last_result, result)
                weaving = True
            else:
                if isinstance(tuple, last_result):
                    p = ''.join(t.group('表層格') for t in last_result)
                    ret.add(p)
                last_result = None
                weaving = False
    return ret

if __name__ == '__main__':
    print('No-phrases:\n', ', '.join(extract_no_phases()))
