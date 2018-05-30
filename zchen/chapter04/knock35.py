from knock30 import *

def extract_noun_strings():
    ret = set()
    for line in line_gen():
        result = re_fields.match(line)
        last_result = None
        if result:
            if result.group('品詞') == '名詞':
                if isinstance(tuple, last_result):
                    last_result = (last_result, result)
                last_result = result
            else:
                if isinstance(tuple, last_result):
                    p = ''.join(t.group('表層格') for t in last_result)
                    ret.add(p)
                last_result = None
    return ret

if __name__ == '__main__':
    print('Noun strings:\n', ', '.join(extract_noun_strings()))
