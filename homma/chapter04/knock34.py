from knock30 import load_morphems_iter

gen1 = load_morphems_iter()
gen2 = load_morphems_iter()
gen3 = load_morphems_iter()
next(gen2)
next(gen3)
next(gen3)

a_no_b = set()
for m1, m2, m3 in zip(gen1, gen2, gen3):
    if m1['pos'] == m3['pos'] == '名詞' and m2['surface'] == 'の':
        a_no_b.add(m1['surface'] + 'の' + m3['surface'])
print(a_no_b)


'''34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．'''
