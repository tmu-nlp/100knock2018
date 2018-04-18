from random import sample
test1 = "I couldn't believe that I could \
actually understand what I was reading : \
the phenomenal power of the human mind ."

def stir_word(w):
    n = len(w)
    if n < 4:
        return w
    return w[0] + "".join(sample(w[1:n-1], n-2)) + w[-1]


def typoglycemia(s):
    los = s.split()
    return " ".join( stir_word(w.strip(". \n\t")) for w in los) + "."

print("Before: %s\nAfter:  %s" % (test1, typoglycemia(test1)))
