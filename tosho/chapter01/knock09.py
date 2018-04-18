import random

def typoglycemia(s):
    words = s.split(' ')
    converted = map(__convert_word, words)
    return ' '.join(converted)

def __convert_word(w):
    if len(w) <= 4:
        return w
    else:
        prefix = w[0]
        surfix = w[-1]
        body = __randomize(list(w[1:-1]))
        return prefix + body + surfix
    
def __randomize(w):
    random.shuffle(w)
    return ''.join(w)

if __name__ == '__main__':
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    r = typoglycemia(s)

    print(s)
    print(r)