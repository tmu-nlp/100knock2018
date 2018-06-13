import sys, os
sys.path.append(os.pardir)
    
from chapter06.knock57 import load_nlp_deps
from collections import defaultdict

if __name__ == '__main__':
    verbs = defaultdict(dict)
    for s_id, deps in load_nlp_deps():
        for dep in deps:
            if dep.dtype == 'nsubj' or dep.dtype == 'dobj':
                verb = dep.governor
                key = f'{s_id}:{verb}'
                verbs[key]['verb'] = verb
                verbs[key][dep.dtype] = dep.dependent

    trim_id = lambda s: s[:s.index('[')]
    print(f'{"verb":<30}{"nsubj":<30}{"dobj"}')
    print('-'*90)
    for name, value in verbs.items():
        if len(value) > 2:
            verb = trim_id(value['verb'])
            nsubj = trim_id(value['nsubj'])
            dobj = trim_id(value['dobj'])
            print(f'{verb:<30}{nsubj:<30}{dobj}')