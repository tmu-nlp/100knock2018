

def create_word_counts(s):
    s = s.replace(',', '')
    s = s.replace('.', '')

    words = s.split(' ')
    l = []
    for word in words:
        l.append(len(word))
    
    return l

if __name__ == '__main__':
    s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    l = create_word_counts(s)
    print(l)
