from utils import non_word

s = "Hi He Lied Because Boron Could Not Oxidize \
Fluorine. New Nations Might Also Sign Peace \
Security Clause. Arthur King Can."

idx_1 = (1, 5, 6, 7, 8, 9, 15, 16, 19)
idx_1 = tuple(i-1 for i in idx_1) # avoid generator !

los = non_word.split(s)
los = filter(len, los)

print(", ".join(
    s[0] if i in idx_1 else (s[:3:2] if i == 11 else s[:2])
        for i, s in enumerate(los)))
