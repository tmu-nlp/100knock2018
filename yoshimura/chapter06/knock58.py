import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

path_sentence = './document/sentences/sentence'
path_dep = './dependencies[@type="collapsed-dependencies"]/dep'

for sentence in tree.iterfind(path_sentence):
    sentence_id = int(sentence.get('id'))
    predicate = {}  # 述語のid : 述語のtxt
    subject = {}  # 述語のid : nsubj関係の子のtxt
    object_ = {}  # 述語のid : dobj関係の子のtxt

    for dep in sentence.iterfind(path_dep):
        gove = dep.find('./governor')
        depe = dep.find('./dependent')
        pre_id = gove.get('idx')

        if dep.get('type') == 'nsubj':
            predicate[pre_id] = gove.text
            subject[pre_id] = depe.text

        elif dep.get('type') == 'dobj':
            predicate[pre_id] = gove.text
            object_[pre_id] = depe.text

    for pre_id, pre_txt in predicate.items():
        # nsubj関係とdobj関係にある子を持つ時のみ表示
        if pre_id in subject and pre_id in object_:
            print(f'{subject[pre_id]}\t{pre_txt}\t{object_[pre_id]}')

    
