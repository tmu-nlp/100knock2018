s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

one_words = [1, 5, 6, 7, 8, 9, 15, 16, 19]
one_words = map(lambda x: x - 1, one_words)

s = s.replace(',', '')
s = s.replace('.', '')

m = {}
for i, word in enumerate(s.split(' ')):
    if i in one_words:
        key = word[0]
    else:
        key = word[:2]
    
    m[key] = len(word)

print(m)