from knock30 import *

def extract_verb_bases():
    verbs = set()
    for line in line_gen():
        result = re_fields.match(line)
        if result and result.group('品詞') == '動詞':
            verbs.add(result.group('原形'))
    return verbs

if __name__ == '__main__':
    print('Base form of verbs:\n', ', '.join(extract_verb_bases()))
