from knock30 import *

def extract_verb_surfaces():
    verbs = set()
    for line in line_gen():
        result = re_fields.match(line)
        if result and result.group('品詞') == '動詞':
            verbs.add(result.group('表層形'))
    return verbs

if __name__ == '__main__':
    print("Using regex:", re_str)
    s = 'Verbs:\n'
    s += ', '.join(extract_verb_surfaces())
    print(s)
